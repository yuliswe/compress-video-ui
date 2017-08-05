import QtQuick 2.7
import QtQuick.Controls 2.2

Item {
    id: fileDelegate
    property var fileListModel: [];
    ConfirmDialog {
        id: confirmDialog
        displayText: "确认要终止转换 \"" + fileUrl + "\" 吗?"
        onAccepted: {
           fileListModel.remove(index, 1);
        }
    }
    height: 64;
    anchors.left: parent.left;
    anchors.right: parent.right;
    anchors.leftMargin: 10;
    Item {
        anchors.fill: parent;
        anchors.topMargin: 5;
        Image {
            id: img
            function whichImg() {
                switch (fileStatus) {
                case mainWindow.enumFileInQueue: return "../img/video-await.png";
                case mainWindow.enumFileInProgress: return "../img/video-convert.png";
                case mainWindow.enumFileToBeAdded: return "../img/video-add.png";
                case mainWindow.enumFileDone: return "../img/video-done.png";
                case mainWindow.enumFileError: return "../img/video-error.png";
                case mainWindow.enumFileUserStop: return "../img/video-warning.png";
                }
            }
            fillMode: Image.PreserveAspectFit
            sourceSize.height: 128;
            sourceSize.width: 128;
            source: img.whichImg();
            anchors.bottom: parent.bottom;
            anchors.left: parent.left;
            anchors.verticalCenter: parent.verticalCenter;
        }
        Label {
            id: fileUrlLabel
            text: fileUrl
            anchors.top: parent.top
            anchors.topMargin: 12
            anchors.leftMargin: 15
            anchors.left: img.right
            font.family: "DengXian"
            font.pixelSize: 11
            elide: Text.ElideMiddle
            anchors.right: progressBar.visible ? progressBar.left : trash.left
        }
        Label {
            id: fileSizeLabel
            text: fileSize
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
            visible: fileStatus == 2;
            anchors.bottom: fileUrlLabel.bottom
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
            visible: fileStatus == 2;
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
                    if (fileStatus === mainWindow.enumFileInProgress) {
                        confirmDialog.open();
                    } else {
                        mainWindow.signalDeleteCurrentTask(fileUrl);
                        fileDelegate.fileListModel.remove(index, 1);
                    }
                }
            }
        }
    }
}
