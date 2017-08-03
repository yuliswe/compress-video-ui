import QtQuick 2.7
import QtQuick.Controls 2.2

Rectangle {
    id: rectangle
    height: 64;
    anchors.left: parent.left;
    anchors.right: parent.right;
    anchors.leftMargin: 10;
    Image {
        id: img
        function whichImg() {
            var tb = [
                        "../img/video-await.png",
                        "../img/video-await.png",
                        "../img/video-await.png",
                    ];
            return tb[status];
        }
        fillMode: Image.PreserveAspectFit
        sourceSize.height: 128;
        sourceSize.width: 128;
        source: whichImg();
        anchors.bottom: parent.bottom;
        anchors.left: parent.left;
        anchors.verticalCenter: parent.verticalCenter;
    }
    Label {
        id: filenameLabel
        text: filename
        anchors.top: parent.top
        anchors.topMargin: 15
        anchors.leftMargin: 15
        anchors.left: img.right
        font.family: "DengXian"
        font.pixelSize: 10
        elide: Text.ElideMiddle
        anchors.right: progressBar.left
    }
    Label {
        id: filesizeLabel
        text: filesize
        anchors.bottomMargin: 15
        anchors.leftMargin: 15
        anchors.left: img.right
        anchors.bottom: parent.bottom
        font.family: "DengXian"
    }
    ProgressBar {
        id: progressBar
        anchors.rightMargin: 20
        anchors.leftMargin: 20
        visible: true
        anchors.bottom: filenameLabel.bottom
        anchors.right: trash.left
        value: percentage
        width: 400
    }
    Label {
        id: percentLabel
        text: percentage + "%"
        anchors.rightMargin: 20
        anchors.right: trash.left
        anchors.top: progressBar.bottom
        anchors.topMargin: 5;
        font.family: "DengXian"
    }
    Image {
        id: trash
        fillMode: Image.PreserveAspectFit
        source: "../img/trash.png"
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter;
        sourceSize.height: 64;
        sourceSize.width: 64;
        height: 32;
        anchors.rightMargin: 15
        width: 32;
        opacity: 0.5;
        MouseArea {
            anchors.fill: parent;
            hoverEnabled: true;
            onEntered: {
                trash.opacity = 1;
            }
            onExited: {
                trash.opacity = 0.5;
            }
            onClicked: {
                confirm.open();
            }
        }
    }
    Dialog {
        id: confirm
        parent: mainWindow.overlay
        implicitHeight: 100;
        implicitWidth: 400;
        standardButtons: Dialog.Ok | Dialog.Cancel;
        leftMargin: parent.width / 2 - width / 2
        topMargin: parent.height / 2 - height / 2 - 30
        header: Text {
            text: "确认要取消转换 \"" + filename + "\" 吗?"
            font.family: "DengXian"
            font.pixelSize: 12
            anchors.left: parent.left
            anchors.leftMargin: 20
            anchors.top: parent.top
            anchors.topMargin: 20
        }
        background: Rectangle {
            border.width: 1;
            border.color: mainWindow.themeColor;
        }
        onAccepted: {
            tasks.whichModel().remove(index, 1);
        }
        onRejected: {}
    }
}
