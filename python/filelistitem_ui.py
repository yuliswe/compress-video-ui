# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin/filelistitem.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FileListItem(object):
    def setupUi(self, FileListItem):
        FileListItem.setObjectName("FileListItem")
        FileListItem.resize(493, 64)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileListItem.sizePolicy().hasHeightForWidth())
        FileListItem.setSizePolicy(sizePolicy)
        FileListItem.setMinimumSize(QtCore.QSize(0, 64))
        FileListItem.setMaximumSize(QtCore.QSize(16777215, 64))
        FileListItem.setStyleSheet("#FileListItem {\n"
"    background-color: transparent;\n"
"}\n"
"#filename, #fileinfo {\n"
"    min-height: 20;\n"
"    max-height: 20;\n"
"}\n"
"#icon {\n"
"    max-height: 64;\n"
"    min-height: 64;\n"
"    max-width: 64;\n"
"    min-width: 64;\n"
"}\n"
"#deleteFileButton {\n"
"    max-height: 32;\n"
"    min-height: 32;\n"
"    max-width: 32;\n"
"    min-width: 32;\n"
"    border: none;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileListItem)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(FileListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setStyleSheet("")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/file.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filename = QtWidgets.QLabel(FileListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)
        self.filename.setStyleSheet("")
        self.filename.setObjectName("filename")
        self.verticalLayout_2.addWidget(self.filename)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileinfo = QtWidgets.QLabel(FileListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileinfo.sizePolicy().hasHeightForWidth())
        self.fileinfo.setSizePolicy(sizePolicy)
        self.fileinfo.setObjectName("fileinfo")
        self.horizontalLayout_2.addWidget(self.fileinfo)
        self.progress = QtWidgets.QProgressBar(FileListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.deleteFileButton = QtWidgets.QToolButton(FileListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteFileButton.sizePolicy().hasHeightForWidth())
        self.deleteFileButton.setSizePolicy(sizePolicy)
        self.deleteFileButton.setMinimumSize(QtCore.QSize(32, 32))
        self.deleteFileButton.setMaximumSize(QtCore.QSize(32, 32))
        self.deleteFileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.deleteFileButton.setIcon(icon)
        self.deleteFileButton.setIconSize(QtCore.QSize(32, 32))
        self.deleteFileButton.setObjectName("deleteFileButton")
        self.horizontalLayout.addWidget(self.deleteFileButton)

        self.retranslateUi(FileListItem)
        QtCore.QMetaObject.connectSlotsByName(FileListItem)

    def retranslateUi(self, FileListItem):
        _translate = QtCore.QCoreApplication.translate
        FileListItem.setWindowTitle(_translate("FileListItem", "Form"))
        self.filename.setText(_translate("FileListItem", "/mydisk/filename.flv"))
        self.fileinfo.setText(_translate("FileListItem", "15MB"))
        self.deleteFileButton.setText(_translate("FileListItem", "..."))

import mainwindow_rc
