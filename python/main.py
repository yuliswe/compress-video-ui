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
         self.filelist.addFile(url.url().replace("file:///", "", 1))

   def setupDragHint(self):
      opacity(self.dragHint, 0.2)

   def setupSidebar(self):
      self.sidebar.setCurrentRow(0)

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

   def closeEvent(self, event):
      event.accept()
      try: self.filelist.killAll()
      except AssertionError: pass
      print("[Application Closed]")


def main():
   threading.currentThread().setName("main")

   appRoot = dirname(abspath(sys.argv[0]))
   print("Running at", appRoot)
   os.chdir(appRoot)
   try:
      app = W.QApplication(sys.argv)
      w = MainWindow()
      app.exec_()
   except Exception as e:
      w.message.error(e)
      print("[Application Error]", e)

main()
