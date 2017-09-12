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
        void signalStartWorker();
        void signalStopWorker();
        void signalStartTasks(QList<File>);
        void signalStopTasks(QList<File>);
        void signalQMLDataChanged(QVariant data);
        void signalWorkerInvoke(QString cmd, QVariant args);

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
        void onWorkerInvoke(QString cmd, QVariant args);

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
