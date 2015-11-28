from PyQt5 import QtWidgets as W
from PyQt5 import QtCore as C
from filelistitem_ui import Ui_FileListItem
import mainwindow_rc

class File(W.QWidget, Ui_FileListItem):
   def __init__(self, parent):
      super().__init__()
      self._debug()
      self.setupUi(self)
      parent.layout().addWidget(self)

   def _debug(self):
      self.name = "example_file_name"
      self.size = "size"
      self.date = "date"
      self.time = "time"


class FileList(W.QListWidget):

   children = []

   def __init__(self, parent):
      super().__init__()
      la = W.QVBoxLayout()
      self.setLayout(la)
      self._debug()
      la.addStretch(1)
      self.setFocusPolicy(0)
      self.setFrameShape(0)
      parent.layout().addWidget(self)

   def _debug(self):
      for f in range(0,3):
         File(self)
