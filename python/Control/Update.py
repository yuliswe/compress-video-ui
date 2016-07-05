from lib.subprocmonitor import *
from lib.lisp import *
import Control.Global as G
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class UpdateChecker(QObject):
   
   SignalUpdateNeeded = pyqtSignal()
   
   def __init__(self, root):
      QObject.__init__(self)
      self.Root = root
      self.Message = root.Message
      self.Dialog = Dialog(self.Root)
      self.SignalUpdateNeeded.connect(self.Dialog.exec)
      self.checkUpdate()

   def checkUpdate(self):
      self.Message.show("检查更新...")
      args = [G.MAIN_OPTIONS.updateBin, "--check-only", G.MAIN_OPTIONS.updateCfg]
      log("Checking update with %s" % " ".join(args))
      updateProcess = SubProcMonitor(cmdArgs=args, final=lambda m:self.promptUpdate(m), pipeErr=True, pipeOut=True)
      updateProcess.start()
      
   def promptUpdate(self, monitor):
      err = monitor.stderr.read()
      log(err)
      if err.find("Application needs an update") != -1:
         self.Message.show("查找到新版本")
         self.SignalUpdateNeeded.emit()
      elif err.find("Application is up-to-date") != -1:
         pass
      elif err.find("Connection refused") != -1:
         self.Message.show("无法连接到网络", 120)
   
   
class Dialog(QDialog):
   
   SignalUpdateCompleted = pyqtSignal()
   
   def __init__(self, Root):
      QDialog.__init__(self)
      layout = QVBoxLayout()
      title = QHBoxLayout()
      text = QHBoxLayout()   
      bottons = QHBoxLayout()   
      layout.addLayout(title)
      layout.addLayout(text)
      layout.addLayout(bottons)
      self.setLayout(layout)
      title.addWidget(QLabel("版本更新"))
      text.addWidget(QLabel("检测到新的版本，是否立即更新? 检测到新的版本，是否立即更新?"))
      bottons.addItem(QSpacerItem(10,10, QSizePolicy.Expanding))
      cancel = QPushButton("取消")
      confirm = QPushButton("立即更新")
      bottons.addWidget(cancel)
      bottons.addWidget(confirm)
      cancel.clicked.connect(self.done)
      
      self.SignalUpdateCompleted.connect(Root.App.quit)
      
      def onConfrim():
         args = [G.MAIN_OPTIONS.updateBin, 
                 G.MAIN_OPTIONS.updateCfg, 
                 "--kill", str(Root.App.applicationPid()),
                 "--install"]
         log("Update with %s" % " ".join(args))
         updateProcess = SubProcMonitor(cmdArgs=args)
         updateProcess.start()
         # self.SignalUpdateCompleted.emit()
      confirm.clicked.connect(onConfrim)
      layout.setContentsMargins(10,10,10,5)
      layout.setSpacing(10)
      