from PyQt5 import QtWidgets as W


class File(W.QWidget):
   def __init__(self, parent):
      super().__init__()
      self._debug()
      self.setLayout(W.QGridLayout())
      self.labels()
      parent.layout().addWidget(self)

   def _debug(self):
      self.name = "example_file_name"
      self.size = "size"
      self.date = "date"
      self.time = "time"

   def labels(self):
      W.QLabel(self.name, self)
      W.QLabel(self.size, self)
      W.QLabel(self.date, self)
      W.QLabel(self.time, self)


class FileList(W.QListWidget):

   children = []

   def __init__(self, parent):
      super().__init__()
      la = W.QVBoxLayout()
      self.setLayout(la)
      self._debug()
      la.addStretch(1)
      parent.layout().addWidget(self)

   def _debug(self):
      for f in [File(self), File(self), File(self)]:
         self.addFile(f)

   def addFile(self, file):
      self.children.append(file)
      self.layout().addWidget(file)

