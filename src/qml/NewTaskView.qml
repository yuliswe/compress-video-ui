import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtGraphicalEffects 1.0

Rectangle {
    id: newTask
    property var selectedStandard: false;
    Label {
        text: "选择要转换到的标准"
        anchors.top: parent.top
        anchors.topMargin: 30
        anchors.left: parent.left
        anchors.leftMargin: 30
        font.family: "DengXian"
        font.pixelSize: 15
    }
    GridLayout {
        anchors.topMargin: 60
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.left: parent.left
        columns: 5;
        Repeater {
            id: repeater
            model: [
                {text: "Acfun", img: "../img/acfun.png", color: mainWindow.themeColor},
                {text: "Bilibili", img: "../img/bilibili.png", color: mainWindow.themeColor},
                {text: "优酷", img: "../img/youku.png", color: mainWindow.themeColor},
            ]
            delegate: Rectangle {
                id: button
                Layout.fillHeight: true;
                Layout.fillWidth: true;
                Layout.minimumHeight: 128;
                Layout.minimumWidth: 128;
                Layout.margins: 30
                Image {
                    id: img
                    source: modelData.img
                    sourceSize.width: 64;
                    sourceSize.height: 64;
                    height: 64;
                    width: 64;
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.verticalCenterOffset: -10
                    visible: false
                }
                ColorOverlay {
                    anchors.fill: img
                    source: img
                    color: modelData.color || "transparent"
                }
                Label {
                    id: label
                    text: modelData.text
                    horizontalAlignment: Text.horizontalAlignment
                    anchors.top: img.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.family: "DengXian"
                    font.pixelSize: 12;
                }
                MouseArea {
                    hoverEnabled: true;
                    anchors.fill: parent;
                    onEntered: {
                        button.color = "#efefef";
                    }
                    onExited: {
                        button.color = "transparent";
                    }
                    onClicked: {
                        newTask.selectedStandard = modelData.text;
                    }
                }
            }
        }
    }
}
