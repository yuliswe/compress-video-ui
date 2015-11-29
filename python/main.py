#!/usr/local/bin/python

import sys
from PyQt5 import QtWidgets as W
from PyQt5 import QtCore
from mainwindow_ui import Ui_MainWindow
import mainwindow_rc
import filelist as F
import types
from lib.qtopacity import opacity

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
         self.filelist.startAll()
         self.startButton.setText("终止")

      def off():
         self.startButton.setChecked(False)
         self.startButton.setText("开始")
         self.filelist.killAll()

      def onClick():
         if self.startButton.isChecked():
            on()
         else:
            off()

      self.filelist.doneSignal.connect(off)
      self.startButton.clicked.connect(onClick)

   def setupFileListArea(self):
      self.filelistArea.setCurrentIndex(0)
      def onAddFile(path):
         self.filelistArea.setCurrentIndex(1)
      self.filelist = F.FileList(self.hasfile)
      self.filelist.addFileSignal.connect(onAddFile)
      # self.filelist._debug()


def main():
   app = W.QApplication(sys.argv)
   MainWindow()
   sys.exit(app.exec_())

main()
