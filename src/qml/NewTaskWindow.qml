import QtQuick 2.7
import QtQuick.Controls 2.2

ApplicationWindow  {
    id: window
    flags: Qt.Tool
    minimumHeight: 400;
    minimumWidth: 600;
    NewTaskView {
        id: newTaskView
        visible: ! newTaskView.selectedStandard
    }
    DropFileView {
        id: dropFileView
        visible: newTaskView.selectedStandard
    }
    function pop() {
        newTaskView.selectedStandard = false;
        window.visible = true;
    }
    title: newTaskView.selectedStandard ? ("转换到" + newTaskView.selectedStandard + "标准格式") : "添加任务"
}
