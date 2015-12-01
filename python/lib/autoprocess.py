from time import sleep
# import multiprocessing as M
import threading as T
from lib.lisp import *

class AutoProcess():

   _killSingal = False
   lock = T.Lock()

   def __init__(self, update, cleanup = nub, frequency = 1):
      self.update = update
      self.frequency = frequency
      self.cleanup = cleanup
      self._process = T.Thread(target=self._do)
      self._process.setDaemon(True)

   def start(self, threadName = "proc"):
      self._process.name = threadName
      self._process.start()
      return self._process

   def join(self):
      self._process.join()

   def kill(self):
      self._killSingal = True

   def _do(self):
      assert T.currentThread().name == self._process.name
      while not self._killSingal:
         with self.lock:
            self.update(self)
         sleep(self.frequency)
      self._killSingal = False
      self.cleanup()
      exit(0)


class Process():
   lock = T.Lock()

   def __init__(self, do, cleanup = nub):
      self.do = do
      self.cleanup = cleanup
      def _do():
         # assert
         assert T.currentThread().name == self._process.name
         # code
         with self.lock:
            self.do()
         self.cleanup()
         exit(0)
      self._process = T.Thread(target=_do)

   def start(self, threadName = "proc"):
      self._process.setDaemon(True)
      self._process.name = threadName
      self._process.start()
      return self._process


def test():
   i = 0
   def do(autoproc):
      nonlocal i
      print(i)
      i = i + 1
      if i > 5:
         autoproc.kill()
   AutoProcess(do).start()
   AutoProcess(do).start()

# test()
