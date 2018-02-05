import QtQuick 2.7
import QtQuick.Controls 2.2
import QtGraphicalEffects 1.0

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
                    {text: "已经完成", img: ""},
//                    {text: "设置", img: ""}
                ]
                delegate: Rectangle {
                    id: button
                    anchors.left: parent.left;
                    anchors.right: parent.right;
                    height: 35
                    color: index === mainWindow.currentView ? mainWindow.navSelectColor : "transparent"
                    Row {
                        id: row
                        spacing: 5
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.leftMargin: 25
                        anchors.verticalCenter: parent.verticalCenter
                        Label {
                            id: label
                            text: modelData.text
                            font.pointSize: 12
                            color: "white"
                            font.family: "DengXian"
                            verticalAlignment: Text.AlignVCenter
                        }
//                        Label {
//                            id: count
//                            text: "9"
//                            font.pointSize: 6
//                            color: "white"
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            width: 15;
//                            height: 13;
//                            background: Rectangle {
//                                color: "grey"
//                                radius: 5
//                            }
//                            visible: true;
//                        }
                    }
                    Rectangle {
//                        radius: 0.5 * width
                        width: 10
                        height: width
                        transform: Rotation { angle: 45 }
                        color: "white"
                        opacity: 1
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.right
                        visible: currentView == index
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
            fileListModel: currentTasksModel
        }
        HistoryTaskView {
            visible: mainWindow.currentView == 1
            fileListModel: historyTasksModel
        }
    }
}
