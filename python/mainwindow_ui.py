# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#centralWidget {\n"
"    background-color: white;\n"
"    spacing: 0;\n"
"}\n"
"")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("#centralWidget {\n"
"    min-width: 600;    \n"
"    min-height: 500;\n"
"    spacing: 0;\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QListWidget(self.centralWidget)
        self.sidebar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.sidebar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet("#sidebar::item:selected {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"#sidebar::item {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: transparent;\n"
"    height: 50px;\n"
"}\n"
"\n"
"#sidebar {\n"
"    border: none;\n"
"    background-color: rgb(255, 104, 132);\n"
"    max-width:150;\n"
"    text-align: center;\n"
"}")
        self.sidebar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.sidebar.setAutoScroll(False)
        self.sidebar.setAutoScrollMargin(0)
        self.sidebar.setProperty("showDropIndicator", False)
        self.sidebar.setDragEnabled(False)
        self.sidebar.setDragDropOverwriteMode(False)
        self.sidebar.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.sidebar.setAlternatingRowColors(False)
        self.sidebar.setTextElideMode(QtCore.Qt.ElideNone)
        self.sidebar.setMovement(QtWidgets.QListView.Static)
        self.sidebar.setFlow(QtWidgets.QListView.TopToBottom)
        self.sidebar.setProperty("isWrapping", False)
        self.sidebar.setResizeMode(QtWidgets.QListView.Fixed)
        self.sidebar.setLayoutMode(QtWidgets.QListView.Batched)
        self.sidebar.setWordWrap(False)
        self.sidebar.setSelectionRectVisible(False)
        self.sidebar.setObjectName("sidebar")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.sidebar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.sidebar.addItem(item)
        self.horizontalLayout.addWidget(self.sidebar)
        self.mainWidget = QtWidgets.QWidget(self.centralWidget)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlBar = QtWidgets.QWidget(self.mainWidget)
        self.controlBar.setAutoFillBackground(False)
        self.controlBar.setStyleSheet("#controlBar {\n"
"    max-height: 30px;\n"
"    border-bottom: 1px solid rgba(0,0,0,0.2);\n"
"}\n"
"QToolButton {\n"
"    border: none;\n"
"    background-color: white;\n"
"}")
        self.controlBar.setObjectName("controlBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.controlBar)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.controlBar)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.configSelector = QtWidgets.QComboBox(self.controlBar)
        self.configSelector.setFocusPolicy(QtCore.Qt.NoFocus)
        self.configSelector.setObjectName("configSelector")
        self.configSelector.addItem("")
        self.horizontalLayout_2.addWidget(self.configSelector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.startButton = QtWidgets.QToolButton(self.controlBar)
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startButton.setStyleSheet("#startButton {\n"
"    padding: 0;\n"
"    margin:0;\n"
"    font-size: 13px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setCheckable(True)
        self.startButton.setChecked(False)
        self.startButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.verticalLayout.addWidget(self.controlBar)
        self.filelistArea = QtWidgets.QStackedWidget(self.mainWidget)
        self.filelistArea.setAcceptDrops(True)
        self.filelistArea.setAutoFillBackground(False)
        self.filelistArea.setStyleSheet("#hasfile {\n"
"    background-color: transparent;\n"
"}")
        self.filelistArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filelistArea.setLineWidth(0)
        self.filelistArea.setObjectName("filelistArea")
        self.nofile = QtWidgets.QWidget()
        self.nofile.setObjectName("nofile")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.nofile)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dragHint = QtWidgets.QWidget(self.nofile)
        self.dragHint.setAcceptDrops(True)
        self.dragHint.setStyleSheet("#dragHintText {\n"
"    font-size: 30px;    \n"
"}\n"
"")
        self.dragHint.setObjectName("dragHint")
        self.gridLayout = QtWidgets.QGridLayout(self.dragHint)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.dragHintText = QtWidgets.QLabel(self.dragHint)
        self.dragHintText.setObjectName("dragHintText")
        self.gridLayout.addWidget(self.dragHintText, 1, 2, 1, 1)
        self.dragHintIcon = QtWidgets.QLabel(self.dragHint)
        self.dragHintIcon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragHintIcon.sizePolicy().hasHeightForWidth())
        self.dragHintIcon.setSizePolicy(sizePolicy)
        self.dragHintIcon.setStyleSheet("#dragHintIcon {\n"
"    max-width: 80px;\n"
"    max-height: 80px;\n"
"}")
        self.dragHintIcon.setText("")
        self.dragHintIcon.setTextFormat(QtCore.Qt.AutoText)
        self.dragHintIcon.setPixmap(QtGui.QPixmap(":/drag.png"))
        self.dragHintIcon.setScaledContents(True)
        self.dragHintIcon.setWordWrap(False)
        self.dragHintIcon.setOpenExternalLinks(False)
        self.dragHintIcon.setObjectName("dragHintIcon")
        self.gridLayout.addWidget(self.dragHintIcon, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        self.horizontalLayout_3.addWidget(self.dragHint)
        self.filelistArea.addWidget(self.nofile)
        self.hasfile = QtWidgets.QWidget()
        self.hasfile.setStyleSheet("QScrollArea {\n"
"    border: none;\n"
"    margin: 0;\n"
"}\n"
"\n"
"")
        self.hasfile.setObjectName("hasfile")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.hasfile)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filelistArea.addWidget(self.hasfile)
        self.verticalLayout.addWidget(self.filelistArea)
        self.notificationArea = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notificationArea.sizePolicy().hasHeightForWidth())
        self.notificationArea.setSizePolicy(sizePolicy)
        self.notificationArea.setStyleSheet("#notificationArea {\n"
"    min-height: 20;\n"
"    max-height: 20;\n"
"}\n"
"#notification {\n"
"    padding-left: 5;\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}")
        self.notificationArea.setObjectName("notificationArea")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.notificationArea)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.notification = QtWidgets.QLabel(self.notificationArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification.sizePolicy().hasHeightForWidth())
        self.notification.setSizePolicy(sizePolicy)
        self.notification.setObjectName("notification")
        self.horizontalLayout_4.addWidget(self.notification)
        self.verticalLayout.addWidget(self.notificationArea)
        self.horizontalLayout.addWidget(self.mainWidget)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.filelistArea.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "压缩不好都是我们的错 － 战xx视频压缩工具"))
        self.sidebar.setSortingEnabled(False)
        __sortingEnabled = self.sidebar.isSortingEnabled()
        self.sidebar.setSortingEnabled(False)
        item = self.sidebar.item(0)
        item.setText(_translate("MainWindow", "Bilibili标准"))
        item = self.sidebar.item(1)
        item.setText(_translate("MainWindow", "自定义"))
        self.sidebar.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "配置文件"))
        self.configSelector.setItemText(0, _translate("MainWindow", "正在加载..."))
        self.startButton.setText(_translate("MainWindow", "开始"))
        self.dragHintText.setText(_translate("MainWindow", "拖入视频文件"))
        self.notification.setText(_translate("MainWindow", "完成 C:movie.flv"))

import mainwindow_rc
