import QtQuick 2.0
import QtQuick.Controls 2.0

ApplicationWindow {
    id: mainWindow
    flags: Qt.FramelessWindowHint
    visible: true
    header: Rectangle {
        border.color: "black"
        border.width: 1
        width: 50
        height: 50
    }
    signal setMouseCursor(int type);
    minimumHeight: 400
    minimumWidth: 600
    MouseArea {
        anchors.fill: parent
        property var clickPos: "0,0"
        property var mode: ""
        property var count: 0
        hoverEnabled: true
        onPressed: {
            clickPos = Qt.point(mouse.x,mouse.y)
            mainWindow.color = "green"
            mode = "drag"
        }
        onReleased: {
            mode = ""
            mainWindow.color = "white"
        }
        onExited: {
            mode = ""
            mainWindow.color = "white"
        }
        onPositionChanged: {
            // monitor resize
            var resizeRight = Math.abs(mouse.x - mainWindow.width) < 30;
            var resizeBottom = Math.abs(mouse.y - mainWindow.height) < 80;
            if (resizeRight && resizeBottom) {
                mode = "resizeDiagnal"
                setMouseCursor(Qt.SizeFDiagCursor);
            } else if (resizeRight) {
                mode = "resizeRight"
                setMouseCursor(Qt.SizeHorCursor);
            } else if (resizeBottom) {
                mode = "resizeBottom"
                setMouseCursor(Qt.SizeVerCursor);
            } else {
                mainWindow.color = "white"
                setMouseCursor(Qt.ArrowCursor);
            }
            if (mode == "drag") {
                var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y)
                mainWindow.x += delta.x
                mainWindow.y += delta.y
            }
        }
    }
}
