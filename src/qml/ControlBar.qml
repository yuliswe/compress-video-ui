import QtQuick 2.7
import QtQuick.Controls 2.2

Rectangle {
    id: controlBar;
    ConfirmDialog {
        id: confirmDialog
        displayText: "确认要终止所有任务? 转换到一半的视频将需要重新转换。"
        onAccepted: {
            for (var i = 0; i < currentTasksModel.count; i++) {
                currentTasksModel.setProperty(i, "fileStatus", mainWindow.enumFileUserStop);
            }
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
//        Repeater {
//            id: repeater
//            model: [
//                {text: "添加视频", img: "", visibleView: [0,1], callback: "newTaskButton", hoverColor: mainWindow.themeColor },
//                {text: "开始转换", img: "", visibleView: [0], hoverColor: mainWindow.themeColor },
//                {text: "全部终止", img: "", visibleView: [0], callback: "stopAllButton", hoverColor: "#C71018" },
//                {text: "清除记录", img: "", visibleView: [1], hoverColor: "#C71018" }
//            ]
//            delegate:
//        }
        ControlBarButton {
            text: "添加视频"
            visible: mainWindow.currentView == 0 || mainWindow.currentView == 1
            hoverColor: mainWindow.themeColor
            callback: newTaskWindow.pop;
        }
        ControlBarButton {
            text: "开始转换"
            visible: {
                for (var i = 0; i < currentTaskView.count; i++) {
                    if (currentTaskView[i].status === mainWindow.enumFileInProgress) {
                        return false;
                    }
                }
                return mainWindow.currentView == 0;
            }
            hoverColor: mainWindow.themeColor
//            callback: {
//                newTaskWindow.pop();
//            }
        }
        ControlBarButton {
            text: "全部终止"
            visible: {
                for (var i = 0; i < currentTaskView.count; i++) {
                    if (currentTaskView[i].status === mainWindow.enumFileInProgress) {
                        return mainWindow.currentView == 0;
                    }
                }
                return false;
            }
            hoverColor: mainWindow.dangerColor
//            callback: newTaskWindow.pop;
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
