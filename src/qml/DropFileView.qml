import QtQuick 2.0

Item {
    id: item1
    anchors.fill: parent;
        Text {
            text: "拖入要转换的文件"
            anchors.rightMargin: -70
            font.family: "DengXian"
            font.pixelSize: 30
            verticalAlignment: Qt.AlignVCenter;
            horizontalAlignment: Qt.AlignRight;
            id: hint
            anchors.right: parent.horizontalCenter;
            anchors.verticalCenter: parent.verticalCenter;
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
