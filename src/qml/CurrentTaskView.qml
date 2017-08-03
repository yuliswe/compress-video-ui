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
                model: [
                    {filename: "file1", status: 0, filesize: "15MB", img: "", eta: ""},
                    {filename: "file1", status: 0, filesize: "15MB", img: "", eta: ""},
                    {filename: "file1", status: 0, filesize: "15MB", img: "", eta: ""},
                    {filename: "file1", status: 0, filesize: "15MB", img: "", eta: ""}
                ]
                delegate: Rectangle {
                    id: rectangle
                    height: 64;
                    anchors.left: parent.left;
                    anchors.right: parent.right;
                    anchors.leftMargin: 10;
                    Image {
                        id: img
                        function useImg() {
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
                        source: modelData.img || useImg();
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
                }
            }
        }
    }
}
