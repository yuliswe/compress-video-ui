from PyQt5 import QtWidgets as W
from PyQt5 import QtCore as C
from filelistitem_ui import Ui_FileListItem
import mainwindow_rc
from lib.filesize import naturalsize
from subprocess import Popen
from autoprocess import AutoProcess, Process
from time import sleep

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

   checked = False
   id = 0

   def __init__(self, parent):
      super().__init__()
      self.setupUi(self)
      self.progress.reset()
      parent.layout().addWidget(self)
      self.progress.valueChanged.connect(self.updateProgressBar)
      self.progress.hide()

   def update(self):
      self.fileinfo.setText(naturalsize(self.size))
      self.filename.setText(self.name)

   def updateProgressBar(self, val):
      self.progress.setValue(val)
      if val == 100:
         self.progress.hide()
      else:
         self.progress.show()

   def stateIs(self, type):
      return isinstance(self.state, type)

   def startProcess(self):
      self.state = File.Running()
      def do():
         self.state.percentage += 10
         self.progress.valueChanged.emit(self.state.percentage)

         print(self.state.percentage)
         if self.state.percentage >= 100:
            self.progress.valueChanged.emit(self.state.percentage)
            self.state = File.Done()

      self.state._process = AutoProcess(lambda: self.stateIs(File.Running), do, .1)
      self.state._process.start()
      return self.state._process

   def killProcess(self):
      self.state._process.kill()


class FileList(W.QListWidget):

   children = []
   _unique = 0
   _shouldKill = False
   doneSignal = C.pyqtSignal()

   def __init__(self, parent):
      super().__init__()
      la = W.QVBoxLayout()
      self.setLayout(la)
      self._debug()
      la.addStretch(1)
      self.setFocusPolicy(0)
      self.setFrameShape(0)
      parent.layout().addWidget(self)

   def _debug(self):
      for i in range(0,3):
         self.addFile("sample_" + str(i))

   def addFile(self, path):
      file = File(self)
      self._unique += 1
      file.id = self._unique
      file.name = path
      file.size = 0
      self.children.append(file)
      file.update()

   def startAll(self):
      self._shouldKill = False
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
