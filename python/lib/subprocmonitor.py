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

   def __init__( self,
                 cmdArgs = None,
                 do = nub,
                 final = nub,
                 frequency = 1,
                 pipeOut = False):
      super(SubProcMonitor, self).__init__()
      self.cmdArgs = cmdArgs
      self.frequency = frequency
      self.do = do
      self.final = final
      self.pipeOut = pipeOut
      # start a thread to check the subprocess repeatedly
      def update(autoproc):
         try:
            # while the subprocess is running
            code = self.subproc.poll()
            if code == None:
               self.do(self)
            # when the subprocess terminates, the monitor terminates
            else:
               if code == 0:
                  self.setSuccess()
                  autoproc.kill()
               else:
                  raise Exception("SubProcMonitor: subprocess returns "+str(self.subproc.poll()))
         except Exception as e:
            if self.subproc.poll() == None: self.kill()
            self.setFailure(e)
            raise e
            
      self.autoproc = AutoProcess(update=update, final=self.final, frequency=self.frequency)

   def start(self, stdout=None, threadName = "monitor"):
      assert self.isAwait(), \
         "SubProcMonitor: Attempted to use a process twice, please allocate a new ProcMonitor."
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
      self.autoproc.start(threadName)

   def kill(self):
      if not self.isRunning():
         warn("SubProcMonitor.kill: SubProcMonitor is "+self.show()+".")
      else:
         self.setFailure("killed")
         if OS.name == 'nt':
            sig = CTRL_BREAK_EVENT 
         elif OS.name == 'posix':
            sig = SIGINT
         self.subproc.send_signal(sig)
         self.subproc.wait()
         
   def join(self):
      if self.isRunning():
         self.subproc.wait()
         if self.autoproc.isRunning(): self.autoproc.join()
         assert not self.subproc.poll() == None, \
            "SubProcMonitor: subprocess still running."
         assert not self.autoproc.isRunning(), \
            "SubProcMonitor: autoproc still running."
      else:
         warn("SubProcMonitor: attempted to join a process that's not running.")
