#ifndef GUI_H
#define GUI_H

#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QCursor>
#include <QSemaphore>
#include "file.h"
#include "worker.h"

class GUI : public QObject {
        Q_OBJECT

    signals:
        void signalDataChanged(QVariant data);

    protected:
        WorkerThread workerThread;
        FileList currentTasksModel;
        FileList historyTasksModel;
        FileList newTasksModel;

    public:
        QVariant getQMLData();
        void notifyDataChanges();
        GUI(int argc, char** argv);
        virtual ~GUI();

    public slots:
        virtual void onDeleteCurrentTask(QString url);
        virtual void onMoveNewTasksToCurrent();
        virtual void onAddNewTasks(QVariant urls);
        virtual void onStartCurrentTasks();
        virtual void onStopCurrentTasks();
};

#endif
