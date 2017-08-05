import QtQuick 2.7
import QtQuick.Controls 2.2
Item {
    anchors.fill: parent;
    DropArea {
        anchors.fill: parent;
        onDropped: {
            console.log(drop.urls);
            signalAddNewTasks(drop.urls);
        }
    }
    Item {
        anchors.fill: parent;
        visible: newTasksModel.count == 0;
        Text {
            text: "拖入视频文件"
            anchors.verticalCenterOffset: -10
            anchors.rightMargin: -40
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
            sourceSize.width: 64;
            height: 64;
            anchors.verticalCenterOffset: 0
            anchors.leftMargin: 20
            width: 64;
            anchors.verticalCenter: hint.verticalCenter
            anchors.left: hint.right
            source: "../img/drop-file.png"
        }
    }
    Item {
        anchors.fill: parent;
        visible: newTasksModel.count > 0;
        Button {
            id: start
            anchors.right: parent.right;
            anchors.bottom: parent.bottom;
            anchors.rightMargin: 40;
            anchors.bottomMargin: 10;
            hoverEnabled: true;

            contentItem: Text {
                color: "black"
                text: "添加到当前任务"
                font.family: "DengXian"
                opacity: enabled ? 1.0 : 0.3
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                elide: Text.ElideRight
            }
            onClicked: {
                var arr = []
                for (var i = 0; i < newTasksModel.count; i++) {
                    newTasksModel.setProperty(i, "fileStatus", mainWindow.enumFileInQueue);
                    arr.push(newTasksModel.get(i).url);
                }
                signalMoveNewTasksToCurrent();
                newTasksModel.clear();
                newTaskWindow.close();
                mainWindow.currentView = 0;
            }
        }
        FileList {
            anchors.fill: null;
            anchors.top: parent.top;
            anchors.left: parent.left;
            anchors.right: parent.right;
            anchors.bottom: start.top;
            anchors.bottomMargin: 5;
            model: newTasksModel;
        }
    }
}
