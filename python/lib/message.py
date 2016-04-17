#coding=utf-8

from PyQt5.QtWidgets import *
from lib.autoprocess import TimeOut
from PyQt5.QtCore import pyqtSignal
from time import sleep
import inspect
from lib import lisp
import traceback
import sys 

class Message():
   height = 25
   showSingal = pyqtSignal()
   hideSingal = pyqtSignal()
   timeOut = None

   def __init__(self, root):
      self.root = root
      self.hide()

   def show(self, text, time = 5):
      self.root.notification.setText(text)
      self.root.notificationArea.show()
      self.timer = time
      if self.timeOut: 
         self.timeOut.kill() 
      # self.timeOut = TimeOut(self.hide, time)

   def hide(self):
      self.root.notificationArea.hide()
      
   def fail(self, text, time = 5):
      return self.show(text, time)

   def error(self, exception, time = 10):
      print("*******", file=sys.stderr)
      lisp.error(exception)
      traceback.print_exc()
      print("*******", file=sys.stderr)
      self.show("发生错误: " + str(exception), time)
