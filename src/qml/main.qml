import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQml 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    AddTaskWindow {
        id: addTaskWindow
    }
    id: mainWindow
    visible: true
    flags: Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint
    // signal setMouseCursor(int type);
    minimumHeight: 500
    minimumWidth: 800
    color: "white"
    property int currentView: 0
    readonly property string navHoverColor: "#2DAD8F";
    readonly property string navColor: "#3DB599";
    readonly property string navSelectColor: "#2DAD8F";
    Rectangle {
        id: nav
        width: 100
        anchors.top: mainWindow.top
        anchors.bottom: mainWindow.bottom
        height: mainWindow.height
        color: "#41a785"
        Column {
            width: parent.width
            height: parent.height
            Repeater {
                id: repeater
                model: [
                    {text: "当前任务", img: "/img/current-tasks.png"},
                    {text: "已完成", img: ""},
                    {text: "设置", img: ""}
                ]
                delegate: Rectangle {
                    id: button
                    width: parent.width
                    height: 35
                    color: index == mainWindow.currentView ? mainWindow.navSelectColor : "transparent"
                    Row {
                        id: rowLayout
                        spacing: 5
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                        Label {
                            id: label
                            text: modelData.text
                            font.pointSize: 9
                            color: "white"
                            font.family: "DengXian"
                            Layout.alignment:  Qt.AlignVCenter | Qt.AlignHCenter
                        }
                    }
                    MouseArea {
                        anchors.fill: parent;
                        hoverEnabled: true;
                        onClicked: {
                            mainWindow.currentView = index;
                            for (var i = 0; i < repeater.count; i++) {
                                if (i !== index) {
                                    repeater.itemAt(i).color = "transparent";
                                } else {
                                    repeater.itemAt(i).color = mainWindow.navSelectColor;
                                }
                            }
                        }
                        onEntered: {
                            if (mainWindow.currentView !== index) {
                                button.color = mainWindow.navHoverColor;
                            }
                        }
                        onExited: {
                            if (mainWindow.currentView !== index) {
                                button.color = "transparent";
                            }
                        }
                    }
                }
            }
        }
    }
    Rectangle {
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: nav.right
        anchors.right: parent.right
        CurrentTaskView {
            visible: mainWindow.currentView == 0;
        }
    }
}
