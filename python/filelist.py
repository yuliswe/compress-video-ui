from PyQt5 import QtWidgets as W
from PyQt5 import QtCore as C
from filelistitem_ui import Ui_FileListItem
import mainwindow_rc
from lib.filesize import naturalsize
from subprocess import Popen
from lib.autoprocess import AutoProcess, Process
from time import sleep
from lib.lisp import *

class File(Ui_FileListItem, W.QWidget):

   class Await():
      """State"""
   class Done():
      stdout = ""
   class Running():
      percentage = 0
      _process = None

   name = ""
   size = 0
   date = [0,0,0]
   time = 0
   state = Await()

   def __init__(self, parent):
      super().__init__()
      self.setupUi(self)
      parent.layout().insertWidget(0, self)
      self.progress.valueChanged.connect(self.updateUI)
      self.initUI()
      #set up deleteFileButton
      # self.deleteFileButton.

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
      return isinstance(self.state, type)

   def startProcess(self):
      assert not self.stateIs(File.Running)

      self.state = File.Running()
      def do():
         self.state.percentage += 10
         self.progress.valueChanged.emit(self.state.percentage)

         print(self.state.percentage)
         if self.state.percentage >= 100:
            self.progress.valueChanged.emit(self.state.percentage)
            self.state = File.Done()

      self.state._process = AutoProcess(lambda: self.stateIs(File.Running), do, 1)
      self.state._process.start()
      return self.state._process

   def killProcess(self):
      self.state._process.kill()
      self.state = File.Done()



class FileList(W.QListWidget):

   children = []
   _unique = 0
   _shouldKill = False
   doneSignal = C.pyqtSignal()
   addFileSignal = C.pyqtSignal([int])

   def __init__(self, parent):
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
         file = File(self)
         self._unique += 1
         file.id = self._unique
         file.name = path
         file.size = 0
         self.children.insert(0,file)
         file.initUI()
         self.addFileSignal.emit(path)

   def startAll(self):
      self._shouldKill = False
      for c in self.children: c.reset()
      def do():
         for idx, c in enumerate(self.children):
            if self._shouldKill:
               break
            print("starting"+str(c))
            p = c.startProcess()
            p.join()
            print("done "+str(c.id))
         self.doneSignal.emit()
      self._process = Process(do)
      self._process.start()

   def killAll(self):
      self._shouldKill = True
      for idx, c in enumerate(self.children):
         if c.stateIs(File.Running):
            c.killProcess()
