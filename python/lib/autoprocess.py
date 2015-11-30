from time import sleep
# import multiprocessing as M
import threading as M
from lib.lisp import *

class AutoProcess():

   _killSingal = False

   def __init__(self, update, cleanup = nub, frequency = 1):
      self.update = update
      self.frequency = frequency
      self.cleanup = cleanup

   def start(self):
      self._process = M.Thread(target=self._do)
      self._process.setDaemon(True)
      self._process.start()
      return self._process

   def join(self):
      self._process.join()

   def kill(self):
      self._killSingal = True

   def _do(self):
      while not self._killSingal:
         self.update(self)
         sleep(self.frequency)
      self._killSingal = False
      self.cleanup()
      exit(0)


class Process():
   def __init__(self, do, cleanup = nub):
      self.do = do
      self.cleanup = cleanup

   def _do(self):
      self.do()
      self.cleanup()

      exit(0)

   def start(self):
      self._process = M.Thread(target=self._do)
      self._process.setDaemon(True)
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
