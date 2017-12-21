import QtQuick 2.7
import QtQuick.Controls 2.2

Dialog {
    id: confirmDialog
    property string displayText: "";
    parent: mainWindow.overlay
    implicitHeight: 100;
    implicitWidth: 400;
    standardButtons: Dialog.Ok | Dialog.Cancel;
    leftMargin: parent.width / 2 - width / 2
    topMargin: parent.height / 2 - height / 2 - 30
    header: Text {
        text: displayText
        font.family: "DengXian"
        font.pixelSize: 12
        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.top: parent.top
        anchors.topMargin: 20
    }
    // Qt bug: <Unknown File>: QML VisualDataModel: Error creating delegate
    // due to setting a custom background
    background: Rectangle {
        border.width: 1;
        border.color: mainWindow.themeColor;
    }
}
