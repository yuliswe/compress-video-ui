from time import sleep
# import multiprocessing as M
import threading as T
from lib.lisp import *
from lib.state import State


class AutoProcess(State):

   lock = T.Lock()

   def __init__(self, update, cleanup = nub, frequency = 1, onError = nub):
      super(AutoProcess, self).__init__()
      self.update = update
      self.frequency = frequency
      self.cleanup = cleanup
      self.onError = onError
      self._process = T.Thread(target=self._do)
      self._process.setDaemon(True)
      self.setAwait()

   def start(self, threadName = "proc"):
      self._process.name = threadName
      self.setRunning()
      self._process.start()

   def join(self):
      self._process.join()
      self.setSuccess()

   def kill(self):
      self.setSuccess()

   def _do(self):
      try:
         assert T.currentThread().name == self._process.name
         while self.isRunning():
            with self.lock:
               self.update(self)
            sleep(self.frequency)
      except Exception as e:
         self.onError(e)
         self.setFailure(e)
      finally:
         self.cleanup()
         exit(0)


class Process(State):

   lock = T.Lock()

   def __init__(self, do, cleanup = nub, onError = nub):
      super(Process, self).__init__()
      self.setAwait()
      self.do = do
      self.cleanup = cleanup
      self.onError = onError
      def _do():
         try:
            # assert
            assert T.currentThread().name == self._process.name
            # code
            with self.lock:
               self.do()
         except Exception as e:
            self.onError(e)
            self.setFailure(e)
         finally:
            self.cleanup()
            exit(0)
      self._process = T.Thread(target=_do)

   def start(self, threadName = "proc"):
      self._process.setDaemon(True)
      self._process.name = threadName
      self._process.start()
      self.setRunning()
      return self._process

class TimeOut():
   def __init__(self, f, time, frequency = 1):
      self.timer = time
      def do(proc):
         if self.timer > 0:
            self.timer -= frequency
         else:
            f()
            proc.kill()
      def onErr(e):
         print e
      self.proc = AutoProcess(do, nub, frequency, onError=onErr)
      self.proc.start()

   def kill(self):
      self.proc.kill()





def test():
   i = 0
   def do(autoproc):
      print(i)
      i = i + 1
      if i > 5:
         autoproc.kill()
   AutoProcess(do).start()
   AutoProcess(do).start()

# test()
