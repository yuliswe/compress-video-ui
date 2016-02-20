from time import sleep
# import multiprocessing as M
import threading as T
from lib.lisp import *
from lib.state import State


class AutoProcess(State):

   def __init__(self, update, final = nub, frequency = 1, count = None, onError = showError):
      super(AutoProcess, self).__init__()
      self.update = update
      self.frequency = frequency
      self.final = final
      self.onError = onError
      self.count = count
      self._process = T.Thread(target=self._do)
      self._process.setDaemon(True)

   def start(self, threadName = "proc"):
      if not self.isAwait():
         warn("AutoProcess.start: process is "+self.show()+".")
      else:
         self._process.name = threadName
         self.setRunning()
         self._process.start()

   def join(self):
      if not self.isRunning():
         warn("AutoProcess.join: process is "+self.show()+".")
      else:
         self._process.join()
         self.setSuccess()

   def kill(self):
      if not self.isRunning():
         warn("AutoProcess.kill: process is "+self.show()+".")
      else:
         self.setFailure("killed")

   def _do(self):
      try:
         assert T.currentThread().name == self._process.name
         while self.isRunning() and (self.count == None or self.count > 0):
            self.update(self)
            if self.count: self.count -= 1
            sleep(self.frequency)
      except Exception as e:
         self.setFailure(e)
         self.onError(e)
      finally:
         self.final()
         exit(0)


class TimeOut():
   def __init__(self, do, time, frequency = 1):
      self.timer = time
      def update(proc):
         if self.timer > 0:
            self.timer -= frequency
         else:
            do()
            proc.kill()
      self.proc = AutoProcess(update=update, 
                              frequency=frequency, 
                              onError=showError)
      self.proc.start('timeout')

   def kill(self):
      if self.proc.isRunning():
         self.proc.kill()


def test():
   i = 0
   def do(autoproc):
      print(i)
      i = i + 1
      if i > 5:
         autoproc.kill()
   AutoProcess(do).start("test")
   AutoProcess(do).start("test")

