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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        MainWindow.setFont(font)
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
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("#centralWidget {\n"
"    min-width: 600;    \n"
"    min-height: 500;\n"
"    spacing: 0;\n"
"    margin: 0;\n"
"    background: white;\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.controlBar = QtWidgets.QWidget(self.centralWidget)
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
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.controlBar)
        self.horizontalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.controlBar)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.configSelector = QtWidgets.QComboBox(self.controlBar)
        self.configSelector.setFocusPolicy(QtCore.Qt.NoFocus)
        self.configSelector.setObjectName("configSelector")
        self.configSelector.addItem("")
        self.horizontalLayout_9.addWidget(self.configSelector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.startButton = QtWidgets.QToolButton(self.controlBar)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startButton.setStyleSheet("#startButton {\n"
"    padding: 0;\n"
"    margin:0;\n"
"    font-size: 13px;\n"
"    background: transparent;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QtCore.QSize(20, 20))
        self.startButton.setCheckable(True)
        self.startButton.setChecked(False)
        self.startButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.startButton.setAutoRaise(True)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_9.addWidget(self.startButton)
        self.gridLayout.addWidget(self.controlBar, 1, 1, 1, 2)
        self.notificationArea = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notificationArea.sizePolicy().hasHeightForWidth())
        self.notificationArea.setSizePolicy(sizePolicy)
        self.notificationArea.setStyleSheet("#notificationArea {\n"
"    min-height: 20;\n"
"    max-height: 20;\n"
"}\n"
"#notification {\n"
"    padding-left: 5px;\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}")
        self.notificationArea.setObjectName("notificationArea")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.notificationArea)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.notification = QtWidgets.QLabel(self.notificationArea)
        self.notification.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification.sizePolicy().hasHeightForWidth())
        self.notification.setSizePolicy(sizePolicy)
        self.notification.setObjectName("notification")
        self.horizontalLayout_10.addWidget(self.notification)
        self.gridLayout.addWidget(self.notificationArea, 3, 1, 1, 2)
        self.sidebar = QtWidgets.QListWidget(self.centralWidget)
        self.sidebar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sidebar.setFont(font)
        self.sidebar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sidebar.setToolTip("")
        self.sidebar.setStatusTip("")
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet("#sidebar::item:selected {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"#sidebar::item {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    width: 100%;\n"
"}\n"
"\n"
"#sidebar {\n"
"    border: none;\n"
"    background-color: rgb(255, 104, 132);\n"
"    text-align: center;\n"
"}")
        self.sidebar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar.setLineWidth(0)
        self.sidebar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sidebar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sidebar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.sidebar.setAutoScroll(False)
        self.sidebar.setAutoScrollMargin(0)
        self.sidebar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sidebar.setProperty("showDropIndicator", False)
        self.sidebar.setDragEnabled(False)
        self.sidebar.setDragDropOverwriteMode(False)
        self.sidebar.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.sidebar.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sidebar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.sidebar.setIconSize(QtCore.QSize(40, 40))
        self.sidebar.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.sidebar.setMovement(QtWidgets.QListView.Static)
        self.sidebar.setFlow(QtWidgets.QListView.TopToBottom)
        self.sidebar.setProperty("isWrapping", False)
        self.sidebar.setResizeMode(QtWidgets.QListView.Adjust)
        self.sidebar.setLayoutMode(QtWidgets.QListView.Batched)
        self.sidebar.setViewMode(QtWidgets.QListView.IconMode)
        self.sidebar.setModelColumn(0)
        self.sidebar.setUniformItemSizes(False)
        self.sidebar.setWordWrap(False)
        self.sidebar.setSelectionRectVisible(True)
        self.sidebar.setObjectName("sidebar")
        item = QtWidgets.QListWidgetItem()
        item.setText("Bilibili标准")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bilibili.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.sidebar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        item.setFont(font)
        self.sidebar.addItem(item)
        self.gridLayout.addWidget(self.sidebar, 0, 0, 4, 1)
        self.filelistArea = QtWidgets.QStackedWidget(self.centralWidget)
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
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.nofile)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dragHint = QtWidgets.QWidget(self.nofile)
        self.dragHint.setAcceptDrops(True)
        self.dragHint.setStyleSheet("#dragHintText {\n"
"    font-size: 30px;    \n"
"}\n"
"")
        self.dragHint.setObjectName("dragHint")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dragHint)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)
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
        self.gridLayout_3.addWidget(self.dragHintIcon, 1, 1, 1, 1)
        self.dragHintText = QtWidgets.QLabel(self.dragHint)
        self.dragHintText.setObjectName("dragHintText")
        self.gridLayout_3.addWidget(self.dragHintText, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 2, 2, 1, 1)
        self.horizontalLayout_8.addWidget(self.dragHint)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.hasfile)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filelistArea.addWidget(self.hasfile)
        self.gridLayout.addWidget(self.filelistArea, 2, 1, 1, 2)
        self.filelistArea.raise_()
        self.controlBar.raise_()
        self.notificationArea.raise_()
        self.sidebar.raise_()
        self.dragHint.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.sidebar.setCurrentRow(0)
        self.filelistArea.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "配置文件"))
        self.configSelector.setItemText(0, _translate("MainWindow", "正在加载..."))
        self.startButton.setText(_translate("MainWindow", "开始"))
        self.notification.setText(_translate("MainWindow", "完成 C:movie.flv"))
        self.sidebar.setSortingEnabled(False)
        __sortingEnabled = self.sidebar.isSortingEnabled()
        self.sidebar.setSortingEnabled(False)
        item = self.sidebar.item(1)
        item.setText(_translate("MainWindow", "自定义"))
        self.sidebar.setSortingEnabled(__sortingEnabled)
        self.dragHintText.setText(_translate("MainWindow", "拖入视频文件"))

import mainwindow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

