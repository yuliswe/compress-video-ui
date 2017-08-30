#ifndef WORKER_H
#define WORKER_H

#include <QThread>
#include <QDebug>
#include <QProcess>
#include <QStringList>
#include <QJsonObject>
#include <QJsonArray>
#include <QList>
#include "file.h"

class WorkerThread : public QThread {
        Q_OBJECT
    signals:
        signalStartWorker();
        signalStopWorker();
        signalStartTasks(QList<File>);
        signalStopTasks(QList<File>);
        signalQMLDataChanged(QVariant data);

    public slots:
        void onStartWorker();
        void onStopWorker();
        void onStartTasks(QList<File>);
        void onStopTasks(QList<File>);
        void onReadyRead();
        void onRemoveCurrentTask(QString url, QString standard);
        void onMoveNewTasksToCurrent();
        void onAddNewTasks(QVariant urls, QString standard);
        void onStartCurrentTasks();
        void onStopCurrentTasks();

    public:
        FileList currentTasksModel;
        FileList historyTasksModel;
        FileList newTasksModel;

        QMap<QString, QProcess> processes;
        QProcess worker;
        bool keepRunning = true;
        WorkerThread();
        ~WorkerThread();
        void run();
        void invoke(QString cmd, QStringList args);
        QVariant getQMLData();
        void notifyDataChanges();
};

#endif // WORKER_H
