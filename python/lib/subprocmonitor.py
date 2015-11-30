from lib.autoprocess import AutoProcess
from subprocess import Popen
from lib.lisp import *

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

   def stateIs(self, type):
      return isinstance(self.state, type)

   def start(self):
      assert not self.stateIs(Running)
      self.state = Running()
      self.state.subproc = Popen(self.cmdArgs)

      # start a thread to check the subprocess repeatedly
      def _do(autoproc):
         assert self.stateIs(Running)
         # when the subprocess terminates, the monitor terminates
         if self.state.subproc.poll() == 0:
            self.state = Success()
            autoproc.kill()
         else:
            self.do(self)

      self.state.monitor = AutoProcess(_do, self.cleanup, self.frequency)
      self.state.monitor.start()

   def kill(self):
      if self.stateIs(Running):
         self.state.subproc.terminate()
         self.state.monitor.kill()
         self.state = Failure()

   def join(self):
      if self.stateIs(Running):
         self.state.monitor.join()
