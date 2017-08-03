import QtQuick 2.7
import QtQuick.Controls 2.2

ApplicationWindow {
    AddTaskWindow {
        id: addTaskWindow
    }
    MainWindowView {}
    id: mainWindow
    visible: true
    flags: Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint
    // signal setMouseCursor(int type);
    minimumHeight: 500
    minimumWidth: 800
    color: "white"
    property int currentView: 0
    readonly property string navHoverColor: "#2DAD8F";
    readonly property string navColor: "#3DB599";
    readonly property string navSelectColor: "#2DAD8F";
    property var currentTasks: [
        {filename: "file1", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file1", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file1", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file1", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""}
    ]
    property var historyTasks: [
        {filename: "file2", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file2", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file2", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""},
        {filename: "file2", status: 0, progress: 0, filesize: "15MB", img: "", eta: ""}
    ]
}
