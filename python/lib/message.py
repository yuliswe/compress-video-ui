#coding=utf-8

from PyQt5.QtWidgets import *
from lib.autoprocess import Process, TimeOut
from PyQt5.QtCore import pyqtSignal
from time import sleep
import inspect

class Message():
   height = 25
   showSingal = pyqtSignal()
   hideSingal = pyqtSignal()
   timeOut = None

   def __init__(self, root):
      self.root = root
      self.hide()

   def show(self, text, time = 10):
      self.root.notification.setText(text)
      self.root.notificationArea.show()
      self.timer = time
      if self.timeOut: self.timeOut.kill()
      self.timeOut = TimeOut(self.hide, time)

   def hide(self):
      self.root.notificationArea.hide()

   def error(self, exception, time = 10):
      print exception
      # for i in inspect.trace():
         # print i
      self.show("发生错误: " + str(exception), time)
      raise exception
