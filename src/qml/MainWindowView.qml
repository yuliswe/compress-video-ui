import QtQuick 2.7
import QtQuick.Controls 2.2

Item {
    anchors.fill: parent;
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
        HistoryTaskView {
            visible: mainWindow.currentView == 1;
        }
    }
}
