# coding=utf-8

from PyQt5.QtWidgets import *
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
import re

class File(Ui_FileListItem, QWidget):

   name = ""
   size = 0
   date = [0,0,0]
   time = 0
   percentage = 0
   message = ""

   monitor = SubProcMonitor()

   _startCalled = 0
   _endCalled = 0

   def __init__(self, root, parent):
      super(File, self).__init__()
      self.root = root
      self.setupUi(self)
      parent.layout().insertWidget(0, self)
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
      self.updateUI(0)

   def updateUI(self, percentage = 0):
      self.fileinfo.setText(naturalsize(self.size)+" "+self.message)
      if self.monitor.isRunning():
         self.progress.show()
         self.progress.setValue(percentage)
      else:
         self.progress.hide()

   def startProcess(self):

      assertThreadIs("FileList.startAll")

      # start a thread to check the progress repeatedly
      def do(monitor):
         assertThreadIs("monitor")

         line = monitor.stdout.readline()
         print(line.strip('\n'))
         input = re.search("percent=(\d+)", line)
         if not input: return

         self.percentage = int(input.group(1))

         self.progress.valueChanged.emit(self.percentage)
         if not self.monitor.isRunning():
            self.progress.valueChanged.emit(self.percentage)
            monitor.kill()

      def onError(e):
         self.monitor.kill()
         self.root.message.error(e)

      args = ['/bin/bash', './bin/testbin']
      # args = ['./bin/compress', self.name, self.name, self.root.configSelector.currentConfig()]
      print(args)
      self.monitor = SubProcMonitor(
         args,
         do,
         pipeOut=True,
         frequency=1,
         onError=onError,
         cleanup=self.killProcess
      )

      self.monitor.start("monitor")

      print("Starts: "+ self.name)
      self._assertBalance()
      self._startCalled += 1


   def killProcess(self):
      # asserts

      self._endCalled += 1
      self._assertBalance()
      print("Finishes: "+ self.name)

      # code
      if not self.monitor.isRunning(): return
      self.monitor.kill()


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
         file.size = 0
         self.children.insert(0,file)
         file.initUI()
         self.addFileSignal.emit(path)

   def startAll(self):
      assertThreadIs("main")

      self._assertBalance()
      self._startCalled += 1

      assert not self.isRunning, \
         "FileList: attempted to start the filelist twice."

      self._shouldKill = False
      self.isRunning = True
      for c in self.children:
         c.reset()

      def do():
         idx = 0
         while idx < len(self.children):
            try:
               c = self.children[idx]
               if self._shouldKill: break
               c.startProcess()
               c.joinProcess()
               assert not c.monitor.isRunning(), \
                  "FileList: file still running."
               assert not c.monitor.isAwait(), \
                  "FileList: file still waiting."
               if c.monitor.isSuccess():
                  self.children.remove(c)
                  self.removeFileSignal.emit(c)
            except Exception as e:
               c.killProcess()
               c.message = "(压缩失败)"
               c.updateUI()
               try: self.root.message.error(e)
               except: pass
               idx += 1

      def clean():
         self.killAll()
         self.doneSignal.emit()

      Process(do, onError=self.root.message.error, cleanup=clean).start("FileList.startAll")
      self.startSignal.emit()

   def removeFile(self, file):
      assertThreadIs("main")
      if file in self.children: self.children.remove(file)
      file.killProcess()
      file.close()

   def killAll(self):

      self._endCalled += 1
      self._assertBalance()

      self._shouldKill = True
      for c in self.children:
         if c.monitor.isRunning(): c.killProcess()
      self.isRunning = False
      self.doneSignal.emit()
