import QtQuick 2.0
import QtQuick.Controls 2.2

ApplicationWindow  {
    id: window
    flags: Qt.Tool
    minimumHeight: 400;
    minimumWidth: 600;
    AddTaskView {
        id: addTaskView
        visible: ! addTaskView.selectedStandard
    }
    DropFileView {
        id: dropFileView
        visible: addTaskView.selectedStandard
    }
    function pop() {
        addTaskView.selectedStandard = false;
        window.visible = true;
    }
    title: addTaskView.selectedStandard ? ("转换到" + addTaskView.selectedStandard + "格式") : "添加任务"
}
