from lib.subprocmonitor import *
from lib.lisp import *
import Control.Global as G

def checkUpdate(self):
   self.Message.show("检查更新...")
   args = [G.MAIN_OPTIONS.updateBin, "--check-only", G.MAIN_OPTIONS.updateCfg]
   log("Checking update with %s" % " ".join(args))
   updateProcess = SubProcMonitor(cmdArgs=args, final=lambda m:promptUpdate(self, m))
   updateProcess.start()
   
def promptUpdate(self, monitor):
   err = monitor.stderr.read()
   log(err)
   if err.find("Application needs an update") != -1:
      self.Message.show("查找到新版本")
   elif err.find("Application is up-to-date") != -1:
      pass
   elif err.find("Connection refused") != -1:
      self.Message.show("无法连接到网络", 120)
      
   