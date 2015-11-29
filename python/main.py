#!/usr/local/bin/python

import sys
from PyQt5 import QtWidgets as W
from PyQt5 import QtCore
from mainwindow_ui import Ui_MainWindow
import mainwindow_rc
import filelist as F

class MainWindow(W.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.setupDragHint()
      self.setupSidebar()
      self.setupFileList()
      self.setupStartButton()
      self.show()

   def setupDragHint(self):
      effect = W.QGraphicsOpacityEffect()
      effect.setOpacity(0.2)
      self.dragHint.setGraphicsEffect(effect)

   def setupSidebar(self):
      self.sidebar.setCurrentRow(0)

   def setupStartButton(self):

      def on():
         self.filelist.startAll()
         self.startButton.setText("终止")
         print("ouch")

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

   def setupFileList(self):
      self.filelist =F.FileList(self.hasfile)


def main():
   app = W.QApplication(sys.argv)
   w = MainWindow()
   sys.exit(app.exec_())

main()
