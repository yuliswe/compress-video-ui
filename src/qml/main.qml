import QtQuick 2.7
import QtQuick.Controls 2.2
//import cpp 1.0

ApplicationWindow {
    // signals
    signal signalRemoveCurrentTask(string fileUrl, string fileStandard);
    signal signalMoveNewTasksToCurrent();
    signal signalAddNewTasks(variant fileUrls, string fileStandard);
    signal signalStartCurrentTasks();
    signal signalStopCurrentTasks();

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
    // global constants
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
    readonly property int enumStandardBilibili: 0;
    readonly property int enumStandardAcFun: 1;
    readonly property int enumStandardYouku: 2;
    // global vars
    property int currentView: 0
    property int inProgressCount: {
        var count = 0;
        for (var i = 0; i < currentTasksModel.count; i++) {
            if (currentTasksModel.get(i).fileStatus === mainWindow.enumFileInProgress) {
                count++;
            }
        }
        return count;
    }
    property int inQueueCount: {
        var count = 0;
        for (var i = 0; i < currentTasksModel.count; i++) {
            if (currentTasksModel.get(i).fileStatus === mainWindow.enumFileInQueue) {
                count++;
            }
        }
        return count;
    }
    property int currentTasksCount: currentTasksModel.count;
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
