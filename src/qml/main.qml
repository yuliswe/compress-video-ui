import QtQuick 2.7
import QtQuick.Controls 2.2
//import cpp 1.0

ApplicationWindow {
    // signals
    signal signalDeleteCurrentTask(string fileUrl);
    signal signalMoveNewTasksToCurrent();
    signal signalAddNewTasks(variant fileUrls);

    NewTaskWindow { id: newTaskWindow }
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
    readonly property string dangerColor: "#C71018";
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
    }
    ListModel {
        id: historyTasksModel
    }
    ListModel {
        id: newTasksModel
    }
    // slots
    Connections {
        target: cpp
        onSignalDataChanged: {
            console.log("onSignalDataChanged", JSON.stringify(data));
            currentTasksModel.clear();
            currentTasksModel.append(data.currentTasksModel);
            historyTasksModel.clear();
            historyTasksModel.append(data.historyTasksModel);
            newTasksModel.clear();
            newTasksModel.append(data.newTasksModel);
        }
    }
}
