import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

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
        anchors.verticalCenter: parent.verticalCenter
        Repeater {
            id: repeater
            model: [
                {text: "添加视频", img: "", visibleView: [0,1], callback: "newTaskButton"},
                {text: "开始转换", img: "", visibleView: [0]},
                {text: "全部终止", img: "", visibleView: [0]},
                {text: "清除记录", img: "", visibleView: [1]}
            ]
            delegate: Rectangle {
                id: button
                width: 75
                height: 40
                function isVisible() {
                    console.log(mainWindow.currentView);
                    return modelData.visibleView.indexOf(mainWindow.currentView) !== -1;
                }
                visible: button.isVisible();
                anchors.verticalCenter: parent.verticalCenter
                color: "transparent"
                Image {
                    visible: true
                    source: modelData.img
                    anchors.verticalCenter: parent.verticalCenter
                }
                Label {
                    text: modelData.text
                    visible: true
                    font.family: "DengXian"
                    verticalAlignment: Qt.AlignVCenter;
                    horizontalAlignment: Qt.AlignHCenter;
                    anchors.fill: parent;
                }
                MouseArea {
                    anchors.fill: parent;
                    hoverEnabled: true;
                    onEntered: {
                        button.color = "grey";
                    }
                    onExited: {
                        button.color = "transparent";
                    }
                    onClicked: {
                        modelData.callback && controlBar[modelData.callback]();
                    }
                }
            }
        }
    }
}
