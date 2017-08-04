import QtQuick 2.7
import QtQuick.Controls 2.2
Item {
    anchors.fill: parent;
    DropArea {
        anchors.fill: parent;
        onDropped: {
            console.log(drop.urls);
        }
    }
    Item {
        anchors.fill: parent;
        visible: addTasksModel.count == 0;
        Text {
            text: "拖入视频文件"
            anchors.rightMargin: -60
            font.family: "DengXian"
            font.pixelSize: 30
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
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: hint.right
            source: "../img/drop-file.png"
        }
    }
    Item {
        anchors.fill: parent;
        visible: addTasksModel.count > 0;
        Button {
            id: start
            anchors.right: parent.right;
            anchors.bottom: parent.bottom;
            anchors.rightMargin: 50;
            anchors.bottomMargin: 30;
            hoverEnabled: true;

            contentItem: Text {
                color: "black"
                text: "开始转换"
                font.family: "DengXian"
                opacity: enabled ? 1.0 : 0.3
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                elide: Text.ElideRight
            }
            //        background: Rectangle {
            //            implicitWidth: 80;
            //            implicitHeight: 20;
            //            color: white;
            //            border.color: start.down ? "#17a81a" : "#2167bf"
            //            border.width: start.hovered ? 1 : 2
            //        }

        }
        Column {
            anchors.fill: parent;
            topPadding: 10;
            Repeater {
                model: addTasksModel;
                delegate: FileDelegate {}
            }
        }
    }
}
