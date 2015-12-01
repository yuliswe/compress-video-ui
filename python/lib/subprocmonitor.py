from lib.autoprocess import AutoProcess
from subprocess import Popen
from lib.lisp import *
import threading as T

class Await():
   """State"""
class Success():
   stdout = ""
class Failure():
   stdout = ""
class Running():
   subproc = None
   monitor = None

class SubProcMonitor():

   state = Await()

   def __init__(self, cmdArgs = None, do = nub, cleanup = nub, frequency = 1):
      self.cmdArgs = cmdArgs
      self.frequency = frequency
      self.do = do
      self.cleanup = cleanup
      # start a thread to check the subprocess repeatedly
      def _do(autoproc):
         assert T.current_thread().name == self.threadName
         assert self.stateIs(Running)
         # when the subprocess terminates, the monitor terminates
         if self.state.subproc.poll() == 0:
            self.state = Success()
            autoproc.kill()
         else:
            self.do(self)
      self.monitor = AutoProcess(_do, self.cleanup, self.frequency)

   def stateIs(self, type):
      return isinstance(self.state, type)

   def start(self, threadName = "monitor"):
      assert not self.stateIs(Running)
      self.threadName = threadName
      self.state = Running()
      self.state.subproc = Popen(self.cmdArgs)
      self.monitor.start(threadName)

   def kill(self):
      if self.stateIs(Running):
         self.monitor.kill()
         self.state.subproc.terminate()
         self.state = Failure()

   def join(self):
      if self.stateIs(Running):
         self.monitor.join()
