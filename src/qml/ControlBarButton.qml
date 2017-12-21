import QtQuick 2.7
import QtQuick.Controls 2.2

Item {
    id: button
    property var text: null
    property var hoverColor: null
    property var callback: null
    width: 75
    anchors.top: parent.top;
    anchors.bottom: parent.bottom;
    //                anchors.verticalCenter: parent.verticalCenter
    //                color: "transparent"
    //                Image {
    //                    visible: true
    //                    source: modelData.img
    //                    anchors.verticalCenter: parent.verticalCenter
    //                }
    Label {
        text: button.text
        visible: true
        font.family: "DengXian"
        verticalAlignment: Qt.AlignVCenter;
        horizontalAlignment: Qt.AlignHCenter;
        anchors.fill: parent;
        font.pixelSize: 11;
    }
    Rectangle {
        id: buttonLine
        anchors.left: parent.left;
        anchors.right: parent.right
        anchors.bottom: button.bottom;
        height: 2
        color: "transparent"
        opacity: 0.8
        z: 2
    }
    MouseArea {
        anchors.fill: parent;
        hoverEnabled: true;
        onEntered: {
            buttonLine.color = button.hoverColor;
        }
        onExited: {
            buttonLine.color = "transparent";
        }
        onClicked: {
            button.callback && button.callback();
        }
    }
}
