import QtQuick 2.7
import QtQuick.Controls 2.2

Rectangle {
    id: controlBar;
    ConfirmDialog {
        id: confirmDialog
        displayText: "确认要终止所有任务? 转换到一半的视频将需要重新转换。"
        onAccepted: {
            mainWindow.signalWorkerInvoke("stopInProgressTasks", []);
        }
    }
    property var fileListModel: [];
    anchors.fill: parent;
    function newTaskButton() {}
    function stopAllButton() {
        if (fileListModel.count > 0) {
            confirmDialog.open();
        }
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
        ControlBarButton {
            text: "添加视频"
            visible: mainWindow.currentView == 0 || mainWindow.currentView == 1
            hoverColor: mainWindow.themeColor
            callback: newTaskWindow.pop;
        }
        ControlBarButton {
            text: "开始转换"
            visible: mainWindow.inProgressCount == 0 && mainWindow.currentView == 0 && currentTasksModel.count > 0;
            hoverColor: mainWindow.themeColor
            callback: function () {
                mainWindow.signalWorkerInvoke("startQueuedOrUserStoppedTasks", []);
            }
        }
        ControlBarButton {
            text: "全部终止"
            visible: mainWindow.inProgressCount > 0 && mainWindow.currentView == 0;
            hoverColor: mainWindow.dangerColor
            callback: confirmDialog.open;
        }
        ControlBarButton {
            text: "清除记录"
            visible: mainWindow.currentView == 1
            hoverColor: mainWindow.dangerColor
            //            callback: {
            //                newTaskWindow.pop();
            //            }
        }
    }
}
