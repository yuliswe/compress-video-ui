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
        FileListItem.resize(449, 64)
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
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileListItem)
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filename = QtWidgets.QLabel(FileListItem)
        self.filename.setStyleSheet("")
        self.filename.setObjectName("filename")
        self.verticalLayout_2.addWidget(self.filename)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileinfo = QtWidgets.QLabel(FileListItem)
        self.fileinfo.setObjectName("fileinfo")
        self.horizontalLayout_2.addWidget(self.fileinfo)
        self.progress = QtWidgets.QProgressBar(FileListItem)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(FileListItem)
        QtCore.QMetaObject.connectSlotsByName(FileListItem)

    def retranslateUi(self, FileListItem):
        _translate = QtCore.QCoreApplication.translate
        FileListItem.setWindowTitle(_translate("FileListItem", "Form"))
        self.filename.setText(_translate("FileListItem", "/mydisk/filename.flv"))
        self.fileinfo.setText(_translate("FileListItem", "15MB"))

import mainwindow_rc
