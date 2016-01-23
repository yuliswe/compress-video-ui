from lib.autoprocess import AutoProcess
from subprocess import *
from lib.lisp import *
from lib.state import State
import threading as T
from lib.state import State
from time import sleep
from signal import *
import os as OS

class SubProcMonitor(State):

   lock = T.Lock()

   def __init__( self,
                 cmdArgs = None,
                 do = nub,
                 cleanup = nub,
                 frequency = 1,
                 pipeOut = False,
                 onError = showError ):
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
            raise e

      self.monitor = AutoProcess(_do, self.cleanup, self.frequency, onError=self.onError)

   def start(self, stdout=None, threadName = "monitor"):
      with self.lock:
         assert not self.isRunning(), \
            "SubProcMonitor: Attempted to start a process twice."
         self.threadName = threadName
         if OS.name == 'posix':
            creationflags = 0
         elif OS.name == 'nt':
            creationflags = CREATE_NEW_PROCESS_GROUP
         self.subproc = Popen(self.cmdArgs, 
                              stdout=PIPE if self.pipeOut else None, 
                              universal_newlines=True,
                              creationflags=creationflags)
         assert self.subproc.pid, \
            "SubProcMonitor: Subprocess could not start."
         self.stdout = self.subproc.stdout
         self.setRunning()
         self.monitor.start(threadName)

   def kill(self):
      if self.isRunning():
         self.monitor.kill()
         if OS.name == 'nt':
            sig = CTRL_BREAK_EVENT 
         elif OS.name == 'posix':
            sig = SIGINT
         if self.subproc.poll() == None:
            self.subproc.send_signal(sig)
            self.subproc.wait()
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
