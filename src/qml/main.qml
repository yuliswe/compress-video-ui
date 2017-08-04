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
    readonly property string themeColor: "#3DB599";
    readonly property string navColor: mainWindow.themeColor;
    readonly property string navSelectColor: "#2DAD8F";
    ListModel {
        id: currentTasksModel
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 2; percentage: 0; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.5; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.4; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 1; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
    }
    ListModel {
        id: historyTasksModel
    }
    ListModel {
        id: addTasksModel
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 0; percentage: 20; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 0; percentage: 0.45; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 0; percentage: 0.74; filesize: "15MB"; img: ""; eta: ""}
        ListElement {filename: "一二三四五六七八九十一二三四五六七八九十"; status: 0; percentage: 0.3; filesize: "15MB"; img: ""; eta: ""}
    }
}
