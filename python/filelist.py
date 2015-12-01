from PyQt5 import QtWidgets as W
from PyQt5 import QtCore as C
from filelistitem_ui import Ui_FileListItem
import mainwindow_rc
from lib.filesize import naturalsize
from subprocess import Popen
from lib.autoprocess import AutoProcess, Process
from time import sleep
from lib.lisp import *
from lib.qtopacity import opacity
from subprocess import Popen
from lib.subprocmonitor import *
import threading as T


class File(Ui_FileListItem, W.QWidget):

   name = ""
   size = 0
   date = [0,0,0]
   time = 0
   percentage = 0

   monitor = SubProcMonitor()

   _startCalled = 0
   _endCalled = 0

   def __init__(self, root, parent):
      self.root = root
      super().__init__()
      self.setupUi(self)
      parent.layout().insertWidget(0, self)
      self.progress.valueChanged.connect(self.updateUI)
      self.initUI()
      #set up deleteFileButton
      opacity(self.deleteFileButton, 0.5)
      self.deleteFileButton.clicked.connect(lambda:parent.removeFile(self))

   def initUI(self):
      self.fileinfo.setText(naturalsize(self.size))
      self.filename.setText(self.name)
      self.reset()

   def reset(self):
      self.progress.reset()
      self.progress.hide()
      self.updateUI(0)

   def updateUI(self, percentage = 0):
      if percentage == 0 or percentage == 100:
         self.progress.hide()
      else:
         self.progress.show()
         self.progress.setValue(percentage)

   def stateIs(self, type):
      return self.monitor.stateIs(type)

   def startProcess(self):
      assert T.current_thread().name == "FileList.startAll"
      assert self._startCalled == self._endCalled
      self._startCalled += 1

      print("./bin/convert " + self.root.configSelector.currentConfig())
      self._ptmp = open("tmp/progress", "w+") # create temp progress file
      self._ptmp.write("0")

      # start a thread to check the progress repeatedly
      def do(monitor):
         assert T.currentThread().name == "monitor"

         intput = self._ptmp.read()
         self._ptmp.seek(0)
         self.percentage = int(self._ptmp.read())
         print(self.percentage)
         self.progress.valueChanged.emit(self.percentage)
         if self.percentage >= 100:
            self.progress.valueChanged.emit(self.percentage)
            self.monitor.kill()
            self.monitor = None

      def cleanup():
         self._ptmp.close()

      self.monitor = SubProcMonitor(['/bin/bash', './bin/testbin', 'tmp/progress'], do, cleanup)

      self.monitor.start("monitor")


   def killProcess(self):
      # asserts
      assert T.current_thread() == T.main_thread() or\
             T.current_thread().name == "FileList.startAll"
      # code
      if not self.stateIs(Running): return
      # asserts
      assert self._startCalled > 0
      self._endCalled += 1
      print(self._startCalled, self._endCalled)
      assert self._startCalled == self._endCalled
      # code
      self.monitor.kill()
      self.monitor = SubProcMonitor()


   def joinProcess(self):
      self.monitor.join()


class FileList(W.QListWidget):

   children = []
   _unique = 0
   _shouldKill = True
   doneSignal = C.pyqtSignal()
   startSignal = C.pyqtSignal()
   addFileSignal = C.pyqtSignal([str])
   removeFileSignal = C.pyqtSignal([str])
   isRunning = False

   _startCalled = 0
   _endCalled = 0

   def __init__(self, root, parent):
      self.root = root
      super().__init__()
      la = W.QVBoxLayout()
      self.setLayout(la)
      la.addStretch(1)
      self.setFocusPolicy(0)
      self.setFrameShape(0)
      parent.layout().addWidget(self)

   def _debug(self):
      for i in range(0,3):
         self.addFile("sample_" + str(i))

   def addFile(self, path):
      if not memberf(lambda x: x.name == path, self.children):
         file = File(self.root, self)
         self._unique += 1
         file.id = self._unique
         file.name = path
         file.size = 0
         self.children.insert(0,file)
         file.initUI()
         self.addFileSignal.emit(path)

   def startAll(self):
      assert T.current_thread() == T.main_thread()

      assert self._startCalled == self._endCalled
      self._startCalled += 1

      assert not self.isRunning

      self._shouldKill = False
      self.isRunning = True
      for c in self.children:
         c.reset()

      def do():
         idx = 0
         while idx < len(self.children):
            c = self.children[idx]
            if self._shouldKill: break
            print("Starts: "+ c.name)
            c.startProcess()
            c.joinProcess()
            print("Finishes: " + c.name)
            if c.stateIs(Success):
               self.removeFile(c)
         self.doneSignal.emit()
      Process(do).start("FileList.startAll")
      self.startSignal.emit()

   def removeFile(self, file):
      file.killProcess()
      self.children.remove(file)
      self.layout().removeWidget(file)
      self.removeFileSignal.emit(file.name)
      file.deleteLater()

   def killAll(self):
      assert T.current_thread() == T.main_thread()
      self._endCalled += 1
      assert self._startCalled == self._endCalled

      self._shouldKill = True
      for c in self.children:
         c.killProcess()
      self.isRunning = False
      self.doneSignal.emit()
