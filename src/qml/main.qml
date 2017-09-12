import QtQuick 2.7
import QtQuick.Controls 2.2
import "../js/ramda.js" as R

ApplicationWindow {
    // signals
    signal signalRemoveCurrentTask(string fileUrl, string fileStandard);
    signal signalMoveNewTasksToCurrent();
    signal signalAddNewTasks(variant fileUrls, string fileStandard);
    signal signalStartCurrentTasks();
    signal signalStopCurrentTasks();
    signal signalWorkerInvoke(string cmd, variant args);

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
    readonly property string enumFileToBeAdded: "Added";
    readonly property string enumFileQueued: "Queued";
    readonly property string enumFileInProgress: "InProgress";
    readonly property string enumFileDone: "Done";
    readonly property string enumFileUserStop: "UserStopped";
    readonly property string enumFileError: "Error";
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
            if (currentTasksModel.get(i).fileStatus === mainWindow.enumFileQueued) {
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
    function updateModel(model, newModel) {
        var oldModel = [];

        for (var j = 0; j < model.count; j++) {
            var obj = model.get(j);
            oldModel.push(obj);
        }

        function cmp(a,b) {
            return a.fileUrl === b.fileUrl && a.fileStandard === b.fileStandard;
        }

        var toRemove = R.differenceWith(cmp, oldModel, newModel);
        var toAdd = R.differenceWith(cmp, newModel, oldModel);
        var toUpdate = R.innerJoin(cmp, newModel, oldModel);

        console.log(oldModel, toAdd, toRemove, toUpdate);

        for (var i = toUpdate.length - 1; i >= 0; i--) {
//            console.log("index", toUpdate[i].index);
            var index = R.findIndex(R.partial(cmp, [toUpdate[i]]), oldModel);
            model.setProperty(index, "fileStatus", toUpdate[i].fileStatus);
            model.setProperty(index, "percentage", toUpdate[i].percentage);
        }

        for (var k = toRemove.length - 1; k >= 0; k--) {
            model.remove(R.findIndex(R.partial(cmp, [toRemove[k]]), oldModel));
        }

        model.append(toAdd);

        //        for (var i = 0; i < newModel.length; i++) {
        //            var found = false;
        //            for (var j = 0; j < model.count; j++) {
        //                if (model.get(j).fileUrl === newModel[i].fileUrl &&
        //                    model.get(j).fileStandard === newModel[i].fileStandard) {
        //                    // update file
        //                    for (var key in newModel[i]) {
        //                        model.setProperty(j, key, newModel[i][key]);
        //                    }
        //                    found = true;
        //                    break;
        //                }
        //            }
        //            if (! found) {
        //                model.insert(0, newModel[i]);
        //            }
        //        }
    }
    Connections {
        target: cpp
        onSignalQMLDataChanged: {
            if (! data) {return;}
            // adopt
            for (var i = 0; i < data.length; i++) {
                data[i].fileStatus = data[i].status;
                data[i].fileUrl = data[i].url;
                data[i].fileStandard = data[i].standard;
                data[i].fileSize = 0;
            }
            console.log("onSignalQMLDataChanged", JSON.stringify(data));
            updateModel(newTasksModel, R.filter(R.propEq("fileStatus", "Added"), data));
            updateModel(currentTasksModel, R.filter(function(e) {
                return R.contains(e.fileStatus, ["Queued", "InProgress", "Error", "Done", "UserStopped"]);
            }, data));
            console.log("currentTasksModel", JSON.stringify(currentTasksModel.get(0)));
            //            historyTasksModel.append(data.historyTasksModel);
        }
    }
}
