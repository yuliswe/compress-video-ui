from time import sleep
# import multiprocessing as M
import threading as M

class AutoProcess():

   _killSingal = False

   def __init__(self, shouldContinue, update, frequency = 1):
      self.shouldContinue = shouldContinue
      self.update = update
      self.frequency = frequency

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
      while self.shouldContinue() and not self._killSingal:
         self.update()
         sleep(self.frequency)
      self._killSingal = False
      exit(0)


class Process():
   def __init__(self, do):
      self.do = do

   def _do(self):
      self.do()
      exit(0)

   def start(self):
      self._process = M.Thread(target=self._do)
      self._process.setDaemon(True)
      self._process.start()
      return self._process


def test():
   i = 0
   def do():
      nonlocal i
      print(i)
      i = i + 1
   AutoProcess(lambda: i < 10, do).start()
   AutoProcess(lambda: i < 5, do).start()

# test()