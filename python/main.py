#!/usr/local/bin/python
# coding=utf-8

import sys
from PyQt5 import QtWidgets as W
from PyQt5.QtCore import *
from mainwindow_ui import Ui_MainWindow
import mainwindow_rc
import filelist as F
import types
from lib.qtopacity import opacity
from control.configfile import ConfigFile
from os.path import abspath, dirname
import os
from lib.message import Message
import threading
from lib.lisp import *

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
      self.message = Message(self)

   def dragEnterEvent(self, event):
      event.accept()

   def dropEvent(self, event):
      event.accept()
      for url in event.mimeData().urls():
         if os.name == 'nt':
            self.filelist.addFile(url.url().replace("file:///", "", 1))
         elif os.name == 'posix':
            self.filelist.addFile(url.url())

   def setupDragHint(self):
      opacity(self.dragHint, 0.2)

   def setupSidebar(self):
      pass
      
   def setupStartButton(self):
      def on():
         self.startButton.setChecked(True)
         self.startButton.setText("终止")
         self.message.show("任务开始")
      def off():
         self.startButton.setChecked(False)
         self.startButton.setText("开始")
         self.message.show("任务结束")
      def onClick():
         if self.startButton.isChecked():
            self.filelist.startAll()
         else:
            self.filelist.killAll()

      self.filelist.startSignal.connect(on)
      self.filelist.doneSignal.connect(off)
      self.startButton.clicked.connect(onClick)

   def setupFileListArea(self):
      self.filelist = F.FileList(self, self.hasfile)
      self.filelist._debug()

   def closeEvent(self, event):
      event.accept()
      self.filelist.killAll()
      log("[Application Closed]")


def main():
   threading.currentThread().setName("main")

   appRoot = dirname(abspath(sys.argv[0]))
   log("Running at " + appRoot)
   os.chdir(appRoot)
   try:
      app = W.QApplication(sys.argv)
      w = MainWindow()
      app.exec_()
   except Exception as e:
      w.message.error(e)
      log("[Application Error]", e)
      raise e

main()
