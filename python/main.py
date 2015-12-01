#!/usr/local/bin/python
# coding=utf-8

import sys
from PyQt5 import QtWidgets as W
from PyQt5 import QtCore
from mainwindow_ui import Ui_MainWindow
import mainwindow_rc
import filelist as F
import types
from lib.qtopacity import opacity
from control.configfile import ConfigFile

def addBetween(parent, target, children):
   for c in children:
      parent.layout().removeWidget(c)
      target.layout().addWidget(c)
      parent.layout().addWidget(target)


class MainWindow(W.QMainWindow, Ui_MainWindow):

   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.setupDragHint()
      self.setupSidebar()
      self.setupFileListArea()
      self.setupStartButton()
      self.show()
      self.setAcceptDrops(True)
      self.configSelector = ConfigFile(self, self.configSelector)

   def dragEnterEvent(self, event):
      event.accept()

   def dropEvent(self, event):
      event.accept()
      for url in event.mimeData().urls():
         self.filelist.addFile(url.path())

   def setupDragHint(self):
      opacity(self.dragHint, 0.2)

   def setupSidebar(self):
      self.sidebar.setCurrentRow(0)

   def setupStartButton(self):
      def on():
         self.startButton.setChecked(True)
         self.startButton.setText("终止")
      def off():
         self.startButton.setChecked(False)
         self.startButton.setText("开始")

      def onClick():
         if self.startButton.isChecked():
            on()
            self.filelist.startAll()
         else:
            off()
            self.filelist.killAll()

      self.filelist.startSignal.connect(on)
      self.filelist.doneSignal.connect(off)
      self.startButton.clicked.connect(onClick)

   def setupFileListArea(self):
      self.filelistArea.setCurrentIndex(0)
      def onRemoveFile(path):
         if len(self.filelist.children) == 0:
            self.filelistArea.setCurrentIndex(0)
      self.filelist = F.FileList(self, self.hasfile)
      self.filelist.addFileSignal.connect(lambda:self.filelistArea.setCurrentIndex(1))
      self.filelist.removeFileSignal.connect(onRemoveFile)
      self.filelist._debug()


def main():
   # try:
      app = W.QApplication(sys.argv)
      w = MainWindow()
      sys.exit(app.exec_())
   # except:
      try: w.filelist.killAll()
      except: pass

main()
