#!/usr/local/bin/python3
# coding=utf-8

import sys
from PyQt5 import QtWidgets as W
from PyQt5.QtCore import *
from mainwindow_ui import Ui_MainWindow
import mainwindow_rc
import filelist as F
import types
from lib.qtopacity import opacity
import os
import os.path as path
from lib.message import Message
import threading
from lib.lisp import *
import argparse
from Control.Preset import *
from Control.Update import *
import Control.Global as G

class MainWindow(W.QMainWindow, Ui_MainWindow):

   def __init__(self, app):
      super(MainWindow, self).__init__()
      self.App = app
      self.setupUi(self)
      self.show()
      self.setupDragHint()
      self.setupSidebar()
      self.setupFileListArea()
      self.setupStartButton()
      self.setAcceptDrops(True)
      self.configSelector = PresetFile(self, self.configSelector)
      # self.setWindowFlags(Qt.FramelessWindowHint)
      self.setupMessage()
      UpdateChecker(self)

   def resizeEvent(self, event):
      # event.ignore()
      self.NotificationArea.resizeEvent(event)
      self.CenterWidgetUpper.resizeEvent(event)

   def dragEnterEvent(self, event):
      event.accept()

   def dropEvent(self, event):
      event.accept()
      for url in event.mimeData().urls():
         if os.name == 'nt':
            self.filelist.addFile(url.url().replace("file:///", "", 1))
         elif os.name == 'posix':
            self.filelist.addFile(url.url().replace("file:///", "/", 1))

   def setupDragHint(self):
      opacity(self.dragHint, 0.2)

   def setupSidebar(self):
      pass

   def setupMessage(self):
      self.Message = Message(self)
      def sizeHint():
         sidebarWidth = self.Sidebar.width()
         windowWidth = self.MainWidget.width()
         return QSize(windowWidth - sidebarWidth, self.Message.height)
      def resizeEvent(event):
         self.NotificationArea.adjustSize()
         self.NotificationArea.move(0, self.MainWidget.height() - self.NotificationArea.height())
      self.NotificationArea.sizeHint = sizeHint
      self.NotificationArea.resizeEvent = resizeEvent
      self.NotificationArea.adjustSize()

   def setupStartButton(self):
      def on():
         self.startButton.setChecked(True)
         self.startButton.setText("终止")
         self.Message.show("任务开始")
      def off():
         self.startButton.setChecked(False)
         self.startButton.setText("开始")
         self.Message.show("任务结束")
      def onClick():
         if self.startButton.isChecked() and self.filelist.children:
            self.filelist.startAll()
         elif (not self.startButton.isChecked()) and self.filelist.children:
            self.filelist.killAll()
         else:
            self.Message.show("当前没有任务")
            self.startButton.setChecked(False)

      self.filelist.startSignal.connect(on)
      self.filelist.doneSignal.connect(off)
      self.startButton.clicked.connect(onClick)

   def setupFileListArea(self):
      def sizeHint():
         sidebarWidth = self.Sidebar.width()
         windowWidth = self.MainWidget.width()
         windowHeight = self.MainWidget.height()
         return QSize(windowWidth - sidebarWidth, windowHeight)
      def resizeEvent(event):
         self.CenterWidgetUpper.adjustSize()
      self.CenterWidgetUpper.sizeHint = sizeHint
      self.CenterWidgetUpper.resizeEvent = resizeEvent
      self.CenterWidgetUpper.adjustSize()
      self.filelist = F.FileList(self, self.hasfile)

   def closeEvent(self, event):
      event.accept()
      self.filelist.killAll()
      log("[Application Closed]")


def main():
   threading.currentThread().setName("main")

   G.MAIN_OPTIONS = G.parseOptions(sys.argv[1:])
   # appRoot = dirname(abspath([0]))
   # os.chdir(appRoot)
   try:
      app = W.QApplication(sys.argv)
      w = MainWindow(app)
      app.exec_()
   except Exception as e:
      w.message.error(e)
      log("[Application Error]", e)
      raise e

main()
