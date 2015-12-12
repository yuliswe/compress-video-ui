from lib.autoprocess import AutoProcess
from subprocess import Popen, PIPE
from lib.lisp import *
from lib.state import State
import threading as T
from lib.state import State
from time import sleep

class SubProcMonitor(State):

   lock = T.Lock()

   def __init__( self,
                 cmdArgs = None,
                 do = nub,
                 cleanup = nub,
                 frequency = 1,
                 pipeOut = False,
                 onError = show ):
      super(SubProcMonitor, self).__init__()
      self.cmdArgs = cmdArgs
      self.frequency = frequency
      self.do = do
      self.cleanup = cleanup
      self.pipeOut = pipeOut
      self.onError = onError
      # start a thread to check the subprocess repeatedly
      def _do(autoproc):
         try:
            assert T.current_thread().name == self.threadName, \
               "SubProcMonitor: wrong thread."
            assert self.isRunning(), \
               "SubProcMonitor: state became "+\
               str(self.state)+ \
               " when the process is "+\
               str(self.subproc)
            if autoproc.isFailure():
               e = autoproc.getException()
               self.onError(e)
               self.setFailure(e)
            # while the subprocess is running
            if self.subproc.poll() == None:
               self.do(self)
            # when the subprocess terminates, the monitor terminates
            elif self.subproc.poll() == 0:
               self.setSuccess()
               autoproc.kill()
               self.cleanup()
            else:
               e = Exception("SubProcMonitor: subprocess returns "+str(self.subproc.poll()))
               self.onError(e)
               self.setFailure(e)
         except Exception as e:
            self.kill()
            self.onError(e)
            self.setFailure(e)

      self.monitor = AutoProcess(_do, self.cleanup, self.frequency, onError=self.onError)

   def start(self, stdout=None, threadName = "monitor"):
      with self.lock:
         assert not self.isRunning(), \
         "SubProcMonitor: Attempted to start a process twice."
         self.threadName = threadName
         self.setRunning()
         self.subproc = Popen(self.cmdArgs, stdout=PIPE if self.pipeOut else None)
         self.stdout = self.subproc.stdout
         self.monitor.start(threadName)

   def kill(self):
      with self.lock:
         if self.isRunning():
            self.monitor.kill()
            if self.subproc.poll() == None:
               self.subproc.terminate()
            self.setSuccess()
            self.cleanup()
            # if self.stdout: self.stdout.close()

   def join(self):
      assert self.isRunning(), \
         "SubProcMonitor: attempted to join a process that's not running."
      self.subproc.wait()
      self.monitor.kill()
      assert not self.monitor.isRunning(), \
         "SubProcMonitor: monitor still running."
      assert not self.subproc.poll() == None, \
         "SubProcMonitor: subprocess still running."
      self.cleanup()
      if self.subproc.poll() == 0:
         self.setSuccess()
      else:
         e = Exception("SubProcMonitor: subprocess returns "+str(self.subproc.poll()))
         self.onError(e)
         self.setFailure(e)
