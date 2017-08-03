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
        Column {
            anchors.fill: parent;
            topPadding: 10;
            Repeater {
                id: repeater
                function whichModel() {
                    var tb = [
                                mainWindow.currentTasks,
                                mainWindow.historyTasks
                            ];
                    return tb[mainWindow.currentView];
                }
                model: repeater.whichModel()
                delegate: FileDelegate {}
            }
        }
    }
}
