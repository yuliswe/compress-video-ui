class Message():
   def __init__(self, parent, ui):
      self.parent = parent
      self.ui = ui

   def show(self, time = 10):
      self.ui.show()

   def hide(self, time = 10):
      self.ui.hide()

