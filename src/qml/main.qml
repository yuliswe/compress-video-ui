import QtQuick 2.7
import QtQuick.Controls 2.2

ApplicationWindow {
    AddTaskWindow { id: addTaskWindow }
    ConfirmDialog { id: confirmDialog }
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
    readonly property string themeColor: "#3DB599";
    readonly property string navColor: mainWindow.themeColor;
    readonly property string navSelectColor: "#2DAD8F";
    readonly property int enumFileToBeAdded: 0;
    readonly property int enumFileInQueue: 1;
    readonly property int enumFileInProgress: 2;
    readonly property int enumFileDone: 3;
    readonly property int enumFileUserStop: 4;
    readonly property int enumFileError: 5;
    ListModel {
        id: currentTasksModel
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十0"; fileStatus: 2; percentage: 0; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十1"; fileStatus: 1; percentage: 0.5; filesize: "15MB"; img: ""; eta: ""}
    }
    ListModel {
        id: historyTasksModel
    }
    ListModel {
        id: addTasksModel
    }
}
