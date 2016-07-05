# coding=utf-8

from os import listdir
import os.path as path
import Control.Global


class PresetFile():
   presets = []
   presetDir = ""

   def __init__(self, root, ui):
      self.root = root
      self.ui = ui
      self.presetDir = Control.Global.MAIN_OPTIONS.presetDir
      self.loadDir(self.presetDir)
      self.updateUI()

   def updateUI(self):
      for i in range(self.ui.count()):
         self.ui.removeItem(i)
      self.ui.addItems([path.basename(f) for f in self.presets])

   def loadFile(self, fp):
      self.presets.append(fp)

   def loadDir(self, fp):
      for p in listdir(fp):
         if not p in [".DS_Store"]: self.loadFile(path.join(fp,p))

   def currentPreset(self):
      return path.join(self.presetDir, self.ui.currentText())
