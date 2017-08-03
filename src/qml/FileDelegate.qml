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
            return tb[modelData.status];
        }
        fillMode: Image.PreserveAspectFit
        sourceSize.height: 128;
        sourceSize.width: 128;
        source: modelData.img || whichImg();
        anchors.bottom: parent.bottom
        anchors.top: parent.top
        anchors.left: parent.left
    }
    Text {
        id: filename
        text: modelData.filename
        anchors.top: parent.top
        anchors.topMargin: 15
        anchors.leftMargin: 15
        anchors.left: img.right
        width: 50;
        font.family: "DengXian"
    }
    Text {
        id: size
        text: modelData.filesize
        anchors.bottomMargin: 15
        anchors.leftMargin: 15
        anchors.left: img.right
        anchors.bottom: parent.bottom
        font.family: "DengXian"
    }
    ProgressBar {
        anchors.rightMargin: 50
        anchors.leftMargin: 20
        visible: true
        anchors.bottom: filename.bottom
        anchors.left: filename.right;
        anchors.right: parent.right;
        value: 0.5
    }
}
