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
        Column {
            anchors.fill: parent;
            topPadding: 10;
            Repeater {
                model: tasks.whichModel()
                delegate: FileDelegate {}
            }
        }
    }
}
