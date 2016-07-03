# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowTitle("压缩不好都是我们的错 － 战xx视频压缩工具")
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        MainWindow.setWindowFilePath("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setMouseTracking(True)
        self.MainWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MainWidget.setAutoFillBackground(False)
        self.MainWidget.setStyleSheet("#centralWidget {\n"
"    min-width: 600;    \n"
"    min-height: 500;\n"
"    spacing: 0;\n"
"    margin: 0;\n"
"    background: white;\n"
"}")
        self.MainWidget.setObjectName("MainWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Sidebar = QtWidgets.QListWidget(self.MainWidget)
        self.Sidebar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sidebar.sizePolicy().hasHeightForWidth())
        self.Sidebar.setSizePolicy(sizePolicy)
        self.Sidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.Sidebar.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sidebar.setFont(font)
        self.Sidebar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Sidebar.setToolTip("")
        self.Sidebar.setStatusTip("")
        self.Sidebar.setAutoFillBackground(False)
        self.Sidebar.setStyleSheet("#Sidebar::item:selected {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"#Sidebar::item {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    width: 100%;\n"
"}\n"
"\n"
"#Sidebar {\n"
"    border: none;\n"
"    background-color: rgb(255, 104, 132);\n"
"    text-align: center;\n"
"}")
        self.Sidebar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Sidebar.setLineWidth(0)
        self.Sidebar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Sidebar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Sidebar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Sidebar.setAutoScroll(False)
        self.Sidebar.setAutoScrollMargin(0)
        self.Sidebar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Sidebar.setProperty("showDropIndicator", False)
        self.Sidebar.setDragEnabled(False)
        self.Sidebar.setDragDropOverwriteMode(False)
        self.Sidebar.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.Sidebar.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Sidebar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.Sidebar.setIconSize(QtCore.QSize(40, 40))
        self.Sidebar.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.Sidebar.setMovement(QtWidgets.QListView.Static)
        self.Sidebar.setFlow(QtWidgets.QListView.TopToBottom)
        self.Sidebar.setProperty("isWrapping", False)
        self.Sidebar.setResizeMode(QtWidgets.QListView.Adjust)
        self.Sidebar.setLayoutMode(QtWidgets.QListView.Batched)
        self.Sidebar.setViewMode(QtWidgets.QListView.IconMode)
        self.Sidebar.setModelColumn(0)
        self.Sidebar.setUniformItemSizes(False)
        self.Sidebar.setWordWrap(False)
        self.Sidebar.setSelectionRectVisible(True)
        self.Sidebar.setObjectName("Sidebar")
        item = QtWidgets.QListWidgetItem()
        item.setText("Bilibili标准")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bilibili.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.Sidebar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        item.setFont(font)
        self.Sidebar.addItem(item)
        self.horizontalLayout.addWidget(self.Sidebar)
        self.CenterWidget = QtWidgets.QWidget(self.MainWidget)
        self.CenterWidget.setStyleSheet("#centerWidget {background: white}")
        self.CenterWidget.setObjectName("CenterWidget")
        self.CenterWidgetUpper = QtWidgets.QWidget(self.CenterWidget)
        self.CenterWidgetUpper.setGeometry(QtCore.QRect(0, 0, 418, 259))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CenterWidgetUpper.sizePolicy().hasHeightForWidth())
        self.CenterWidgetUpper.setSizePolicy(sizePolicy)
        self.CenterWidgetUpper.setObjectName("CenterWidgetUpper")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CenterWidgetUpper)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlBar = QtWidgets.QWidget(self.CenterWidgetUpper)
        self.controlBar.setAutoFillBackground(False)
        self.controlBar.setStyleSheet("#controlBar {\n"
"    max-height: 30px;\n"
"    border-bottom: 1px solid rgba(0,0,0,0.2);\n"
"    background-color: white;\n"
"}\n"
"QToolButton {\n"
"    border: none;\n"
"    background-color: white;\n"
"}\n"
"")
        self.controlBar.setObjectName("controlBar")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.controlBar)
        self.horizontalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.controlBar)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.configSelector = QtWidgets.QComboBox(self.controlBar)
        self.configSelector.setFocusPolicy(QtCore.Qt.NoFocus)
        self.configSelector.setObjectName("configSelector")
        self.configSelector.addItem("")
        self.horizontalLayout_12.addWidget(self.configSelector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.startButton = QtWidgets.QToolButton(self.controlBar)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startButton.setStyleSheet("#startButton {\n"
"    padding: 0;\n"
"    margin:0;\n"
"    font-size: 13px;\n"
"    background: transparent;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QtCore.QSize(20, 20))
        self.startButton.setCheckable(True)
        self.startButton.setChecked(False)
        self.startButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.startButton.setAutoRaise(True)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_12.addWidget(self.startButton)
        self.verticalLayout.addWidget(self.controlBar)
        self.filelistArea = QtWidgets.QStackedWidget(self.CenterWidgetUpper)
        self.filelistArea.setAcceptDrops(True)
        self.filelistArea.setAutoFillBackground(False)
        self.filelistArea.setStyleSheet("#filelistArea {\n"
"    background: white;\n"
"}")
        self.filelistArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filelistArea.setLineWidth(0)
        self.filelistArea.setObjectName("filelistArea")
        self.nofile = QtWidgets.QWidget()
        self.nofile.setObjectName("nofile")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.nofile)
        self.horizontalLayout_11.setContentsMargins(11, 11, 40, 50)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.dragHint = QtWidgets.QWidget(self.nofile)
        self.dragHint.setAcceptDrops(True)
        self.dragHint.setStyleSheet("#dragHintText {\n"
"    font-size: 30px;    \n"
"}\n"
"")
        self.dragHint.setObjectName("dragHint")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dragHint)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 3, 1, 1)
        self.dragHintIcon = QtWidgets.QLabel(self.dragHint)
        self.dragHintIcon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragHintIcon.sizePolicy().hasHeightForWidth())
        self.dragHintIcon.setSizePolicy(sizePolicy)
        self.dragHintIcon.setMaximumSize(QtCore.QSize(80, 80))
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
        self.gridLayout_4.addWidget(self.dragHintIcon, 1, 1, 1, 1)
        self.dragHintText = QtWidgets.QLabel(self.dragHint)
        self.dragHintText.setObjectName("dragHintText")
        self.gridLayout_4.addWidget(self.dragHintText, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 2, 2, 1, 1)
        self.horizontalLayout_11.addWidget(self.dragHint)
        self.filelistArea.addWidget(self.nofile)
        self.hasfile = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hasfile.sizePolicy().hasHeightForWidth())
        self.hasfile.setSizePolicy(sizePolicy)
        self.hasfile.setStyleSheet("QScrollArea {\n"
"    border: none;\n"
"    margin: 0;\n"
"}\n"
"\n"
"")
        self.hasfile.setObjectName("hasfile")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.hasfile)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.filelistArea.addWidget(self.hasfile)
        self.verticalLayout.addWidget(self.filelistArea)
        self.NotificationArea = QtWidgets.QWidget(self.CenterWidget)
        self.NotificationArea.setGeometry(QtCore.QRect(0, 480, 109, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NotificationArea.sizePolicy().hasHeightForWidth())
        self.NotificationArea.setSizePolicy(sizePolicy)
        self.NotificationArea.setStyleSheet("#NotificationArea {\n"
"    min-height: 20;\n"
"    max-height: 20;\n"
"}\n"
"#Notification {\n"
"    padding-left: 5px;\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}")
        self.NotificationArea.setObjectName("NotificationArea")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.NotificationArea)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Notification = QtWidgets.QLabel(self.NotificationArea)
        self.Notification.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Notification.sizePolicy().hasHeightForWidth())
        self.Notification.setSizePolicy(sizePolicy)
        self.Notification.setObjectName("Notification")
        self.horizontalLayout_10.addWidget(self.Notification)
        self.CenterWidgetUpper.raise_()
        self.NotificationArea.raise_()
        self.filelistArea.raise_()
        self.horizontalLayout.addWidget(self.CenterWidget)
        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)
        self.Sidebar.setCurrentRow(0)
        self.filelistArea.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Sidebar.setSortingEnabled(False)
        __sortingEnabled = self.Sidebar.isSortingEnabled()
        self.Sidebar.setSortingEnabled(False)
        item = self.Sidebar.item(1)
        item.setText(_translate("MainWindow", "自定义"))
        self.Sidebar.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "配置文件"))
        self.configSelector.setItemText(0, _translate("MainWindow", "正在加载..."))
        self.startButton.setText(_translate("MainWindow", "开始"))
        self.dragHintText.setText(_translate("MainWindow", "拖入视频文件"))
        self.Notification.setText(_translate("MainWindow", "完成 C:movie.flv"))

import mainwindow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

