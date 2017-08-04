import QtQuick 2.7
import QtQuick.Controls 2.2

Rectangle {
    id: controlBar;
    anchors.fill: parent;
    function newTaskButton() {
        addTaskWindow.pop();
    }
    color: "transparent"
    Rectangle {
        id: line
        anchors.left: parent.left;
        anchors.right: parent.right
        anchors.bottom: parent.bottom;
        height: 1
        color: "lightgrey"
    }
    Row {
        id: row
        anchors.fill: parent;
        Repeater {
            id: repeater
            model: [
                {text: "添加视频", img: "", visibleView: [0,1], callback: "newTaskButton", hoverColor: mainWindow.themeColor },
                {text: "开始转换", img: "", visibleView: [0], hoverColor: mainWindow.themeColor },
                {text: "全部终止", img: "", visibleView: [0], hoverColor: "#C71018" },
                {text: "清除记录", img: "", visibleView: [1], hoverColor: "#C71018" }
            ]
            delegate: Item {
                id: button
                width: 75
                anchors.top: parent.top;
                anchors.bottom: parent.bottom;
                function isVisible() {
                    console.log(mainWindow.currentView);
                    return modelData.visibleView.indexOf(mainWindow.currentView) !== -1;
                }
                visible: button.isVisible();
//                anchors.verticalCenter: parent.verticalCenter
//                color: "transparent"
//                Image {
//                    visible: true
//                    source: modelData.img
//                    anchors.verticalCenter: parent.verticalCenter
//                }
                Label {
                    text: modelData.text
                    visible: true
                    font.family: "DengXian"
                    verticalAlignment: Qt.AlignVCenter;
                    horizontalAlignment: Qt.AlignHCenter;
                    anchors.fill: parent;
                    font.pixelSize: 11;
                }
                Rectangle {
                    id: buttonLine
                    anchors.left: parent.left;
                    anchors.right: parent.right
                    anchors.bottom: button.bottom;
                    height: 2
                    color: "transparent"
                    opacity: 0.8
                    z: 2
                }
                MouseArea {
                    anchors.fill: parent;
                    hoverEnabled: true;
                    onEntered: {
                        buttonLine.color = modelData.hoverColor;
                    }
                    onExited: {
                        buttonLine.color = "transparent";
                    }
                    onClicked: {
                        modelData.callback && controlBar[modelData.callback]();
                    }
                }
            }
        }
    }
}
