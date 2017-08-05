import QtQuick 2.7
import QtQuick.Controls 2.2

ListView {
    id: fileList
    anchors.fill: parent;
    model: []
    boundsBehavior: Flickable.StopAtBounds
    clip: true
    delegate: FileDelegate {
        fileListModel: fileList.model
    }
    ScrollBar.vertical: ScrollBar {
        policy: ScrollBar.AsNeeded
    }
}

