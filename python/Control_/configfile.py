# coding=utf-8

from os import listdir
from os.path import *
import Control.Global


class ConfigFile():
   configs = []
   configDir = ""

   def __init__(self, root, ui):
      self.root = root
      self.ui = ui
      self.configDir = Control.Global.MAIN_OPTIONS.cfgDir
      self.loadDir(self.configDir)
      self.updateUI()

   def updateUI(self):
      for i in range(self.ui.count()):
         self.ui.removeItem(i)
      self.ui.addItems([basename(f) for f in self.configs])

   def loadFile(self, path):
      self.configs.append(path)

   def loadDir(self, path):
      for p in listdir(path):
         if not p in [".DS_Store"]: self.loadFile(path+'/'+p)

   def currentConfig(self):
      return self.configDir + self.ui.currentText()
