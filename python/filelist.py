# coding=utf-8

from PyQt5.QtWidgets import *
from PyQt5 import QtCore as C
from filelistitem_ui import Ui_FileListItem
import mainwindow_rc
from lib.filesize import naturalsize
from subprocess import Popen
from lib.autoprocess import AutoProcess
from time import sleep
from lib.lisp import *
from lib.qtopacity import opacity
from subprocess import Popen
from lib.subprocmonitor import *
import threading as T
import re
import os.path as Path

class File(Ui_FileListItem, QWidget):

   name = ""
   size = 0
   date = [0,0,0]
   time = 0
   percentage = 0
   message = ""

   monitor = None

   _startCalled = 0
   _endCalled = 0

   def __init__(self, root, parent):
      super(File, self).__init__()
      self.root = root
      self.setupUi(self)
      parentL = parent.layout()
      parentL.insertWidget(parentL.count() - 1, self)
      self.progress.valueChanged.connect(self.updateUI)
      self.initUI()
      #set up deleteFileButton
      opacity(self.deleteFileButton, 0.5)
      self.deleteFileButton.clicked.connect(lambda:parent.removeFile(self))

   def _assertBalance(self):
      assert self._startCalled <= self._endCalled, \
         "File: unbalanced start:kill by " + \
         str(self._startCalled - self._endCalled)

   def initUI(self):
      self.fileinfo.setText(naturalsize(self.size))
      self.filename.setText(self.name)
      self.reset()

   def reset(self):
      self.message = ""
      self.progress.reset()
      self.progress.hide()
      self.percentage = 0;
      self.updateUI()

   def updateUI(self):
      self.fileinfo.setText(naturalsize(self.size)+" "+self.message)
      if self.monitor and self.monitor.isRunning():
         self.progress.show()
         self.progress.setFormat("%.1f%%" % self.percentage)
         self.progress.setValue(self.percentage)
      else:
         self.progress.hide()

   def startProcess(self):

      assertThreadIs("FileList.startAll")

      # start a thread to check the progress repeatedly
      def do(monitor):
         assertThreadIs("monitor")
         line = monitor.stdout.readline()
         print(line, end='', file=sys.stderr)
         input = re.search("percent=(\d+\\.?\d*)", line)
         if not input: return
         self.percentage = float(input.group(1))
         self.progress.valueChanged.emit(self.percentage)
            
      def final():
         self._endCalled += 1

      # arg = ['bash', './bin/testbin']
      arg = ["compress", self.name, self.name, self.root.configSelector.currentConfig()]
      log("Arguments: " + " ".join(arg))
      
      self.monitor = SubProcMonitor(
         cmdArgs=arg,
         do=do,
         pipeOut=True,
         frequency=0,
         final=final
      )

      self.monitor.start("monitor")

      log("Started: "+ self.name)
      self._assertBalance()
      self._startCalled += 1


   def killProcess(self):
      if self.monitor and self.monitor.isRunning(): 
         self.monitor.kill()
         log("Finishes: "+ self.name)


   def joinProcess(self):
      self.monitor.join()


class FileList(QListView):

   children = []
   _unique = 0
   _shouldKill = True
   doneSignal = C.pyqtSignal()
   startSignal = C.pyqtSignal()
   addFileSignal = C.pyqtSignal([str])
   removeFileSignal = C.pyqtSignal([File])
   isRunning = False

   gChildH = 74 # child height

   _startCalled = 0
   _endCalled = 0

   def __init__(self, root, parent):
      super(FileList, self).__init__()
      self.root = root
      self.parent = parent
      self.setLayout(QVBoxLayout())
      scroll = QScrollArea()
      parent.layout().addWidget(scroll)
      scroll.setWidget(self)
      self.layout().addStretch(1)
      scroll.setWidgetResizable(True)
      self.setFocusPolicy(0)
      self.setFrameShape(0)
      self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
      # signals
      self.removeFileSignal.connect(self.removeFile)
      self.addFileSignal.connect(lambda:root.filelistArea.setCurrentIndex(1))
      
   def sizeHint(self):
      return C.QSize(0, len(self.children) * self.gChildH)

   def _debug(self):
      for i in range(0,10):
         self.addFile("sample_" + str(i))

   def _assertBalance(self):
      assert self._startCalled <= self._endCalled, \
         "unbalanced startAll killAll by " + \
         str(self._startCalled - self._endCalled)

   def addFile(self, path):
      if not memberf(lambda x: x.name == path, self.children):
         file = File(self.root, self)
         self._unique += 1
         file.id = self._unique
         file.name = path
         file.size = Path.getsize(path) if Path.exists(path) else 0
         self.children.append(file)
         file.initUI()
         self.addFileSignal.emit(path)

   def startAll(self):
      log("FileList.startAll()")
      assertThreadIs("main")

      self._assertBalance()
      self._startCalled += 1

      for c in self.children:
         if c._startCalled != c._endCalled:
            error("Please wait for "+str(c)+" to finish running.")
            return
      assert not self.isRunning, \
         "FileList: attempted to start the filelist twice."

      self._shouldKill = False
      self.isRunning = True
      for c in self.children:
         c.reset()

      def do(proc):
         idx = 0
         while idx < len(self.children):
            try:
               c = self.children[idx]
               if self._shouldKill: break
               c.startProcess()
               c.joinProcess()
               assert not c.monitor.isRunning(), \
                  "FileList: file still running."
               if c.monitor.isSuccess():
                  self.children.remove(c)
                  self.removeFileSignal.emit(c)
               else:
                  c.message = "压缩失败"
                  c.updateUI()
                  idx += 1
               
            except Exception as e:
               c.killProcess()
               c.message = "压缩失败"
               c.updateUI()
               self.root.message.error(e)
               idx += 1
               raise e
               
      def final():
         self._endCalled += 1
         self.doneSignal.emit()

      AutoProcess(update=do, 
                  count=1, 
                  final=final).start("FileList.startAll")
      self.startSignal.emit()
      self.isRunning = False

   def removeFile(self, file):
      assertThreadIs("main")
      if file in self.children:
         self.children.remove(file)
      file.killProcess()
      file.close()
      if not self.children:
         self.root.filelistArea.setCurrentIndex(0)

   def killAll(self):
      self._endCalled += 1
      self._assertBalance()

      self._shouldKill = True
      for c in self.children:
         c.killProcess()
      self.isRunning = False
      