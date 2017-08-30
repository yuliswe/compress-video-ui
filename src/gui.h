#ifndef GUI_H
#define GUI_H

#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QCursor>
#include <QJsonObject>
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
        virtual void onRemoveCurrentTask(QString url, QString standard);
        virtual void onMoveNewTasksToCurrent();
        virtual void onAddNewTasks(QVariant urls, QString standard);
        virtual void onStartCurrentTasks();
        virtual void onStopCurrentTasks();
        virtual void onAboutToQuit();
        virtual void onProgressChanged(QJsonArray obj);
};

#endif
