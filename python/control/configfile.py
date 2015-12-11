# coding=utf-8

from os import listdir
from os.path import basename

class ConfigFile():

   configs = []

   def __init__(self, root, ui):
      self.root = root
      self.ui = ui
      self.loadDir('./config')
      self.updateUI()

   def updateUI(self):
      for i in range(self.ui.count()):
         self.ui.removeItem(i)
      self.ui.addItems([basename(f) for f in self.configs])

   def loadFile(self, path):
      self.configs.append(path)

   def loadDir(self, path):
      for p in listdir(path):
         self.loadFile(path+'/'+p)

   def currentConfig(self):
      return './config/'+self.ui.currentText()
