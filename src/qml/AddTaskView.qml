import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

Rectangle {
    id: addTask
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
                {text: "bilibili", img: ""},
                {text: "bilibili", img: ""},
                {text: "bilibili", img: ""},
                {text: "bilibili", img: ""},
                {text: "bilibili", img: ""},
                {text: "bilibili", img: ""}
            ]
            delegate: Rectangle {
                id: button
                Layout.fillHeight: true;
                Layout.fillWidth: true;
                Layout.minimumHeight: 50;
                Layout.minimumWidth: 50;
                Layout.margins: 30
                Image {
                    source: modelData.img
                }
                Label {
                    id: label
                    text: modelData.text
                }
                MouseArea {
                    hoverEnabled: true;
                    anchors.fill: parent;
                    onEntered: {
                        button.color = "lightgrey";
                    }
                    onExited: {
                        button.color = "transparent";
                    }
                    onClicked: {
                        addTask.selectedStandard = modelData.text;
                    }
                }
            }
        }
    }
}
