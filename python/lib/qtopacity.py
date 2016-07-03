from PyQt5 import QtWidgets as W

def opacity(target, val):
   effect = W.QGraphicsOpacityEffect()
   effect.setOpacity(val)
   target.setGraphicsEffect(effect)
