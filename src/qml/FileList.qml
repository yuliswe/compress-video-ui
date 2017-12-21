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
    ConfirmDialog {
        id: confirmDialog
        property string fileUrl: "";
        property string fileStandard: "";
        displayText: "确认要终止转换 \"" + this.fileUrl + "\"(" + this.fileStandard + ") 吗?"
        onAccepted: {
            mainWindow.signalWorkerInvoke("removeTask", [this.fileUrl, this.fileStandard]);
        }
    }
}

