import QtQuick 2.7
import QtQuick.Controls 2.2

ListView {
    anchors.fill: parent;
    model: []
    boundsBehavior: Flickable.StopAtBounds
    clip: true
    delegate: FileDelegate {}
    ScrollBar.vertical: ScrollBar {
        policy: ScrollBar.AlwaysOn
    }
}

