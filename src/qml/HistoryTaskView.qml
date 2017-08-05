import QtQuick 2.7
import QtQuick.Controls 2.2
Item {
    anchors.fill: parent
    id: historyTaskView
    property var fileListModel: []
    CurrentTaskView {
        fileListModel: historyTaskView.fileListModel
    }
}

