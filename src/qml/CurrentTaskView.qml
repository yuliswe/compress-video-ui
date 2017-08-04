import QtQuick 2.7
import QtQuick.Controls 2.2

Item {
    anchors.fill: parent;
    Rectangle {
        anchors.top: parent.top
        anchors.right: parent.right;
        anchors.left: parent.left;
        anchors.bottom: tasks.top;
        ControlBar {
            anchors.fill: parent;
        }
    }
    Rectangle {
        id: tasks
        anchors.top: parent.top
        anchors.topMargin: 30
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        function whichModel() {
            var tb = [
                        currentTasksModel,
                        historyTasksModel
                    ];
            return tb[mainWindow.currentView];
        }
        ListView {
            anchors.fill: parent;
            model: tasks.whichModel()
            boundsBehavior: Flickable.StopAtBounds
            clip: true
            delegate: FileDelegate {}
            ScrollBar.vertical: ScrollBar {
                policy: ScrollBar.AlwaysOn
            }
        }
        Item {
            anchors.fill: parent;
            visible: tasks.whichModel().count === 0;
            Item {
                anchors.fill: parent;
                Text {
                    text: "这里还没有任务哦"
                    anchors.verticalCenterOffset: -10
                    font.bold: false
                    anchors.rightMargin: -60
                    font.family: "DengXian"
                    font.pixelSize: 27
                    verticalAlignment: Qt.AlignVCenter;
                    horizontalAlignment: Qt.AlignRight;
                    id: hint
                    anchors.right: parent.horizontalCenter;
                    anchors.verticalCenter: parent.verticalCenter;
                    opacity: 0.5;
                }
                Image {
                    sourceSize.height: 64;
                    sourceSize.width: 64
                    height: 64;
                    fillMode: Image.Stretch
                    anchors.verticalCenterOffset: -10
                    anchors.leftMargin: 20
                    width: 70
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: hint.right
                    source: "../img/empty.png"
                    opacity: 0.8;
                }
            }
            Item {
                opacity: 0.5;
                anchors.fill: parent;
                Text {
                    x: 89
                    y: 37
                    text: "点击这里"
                    font.family: "DengXian"
                    font.pixelSize: 12
                }
                Image {
                    x: 86
                    y: 84
                    sourceSize.height: 64;
                    sourceSize.width: 64
                    height: 64;
                    width: 70
                    source: "../img/arrow.png"
                    transform: Rotation { angle: 200 }
                }
            }
        }
    }
}
