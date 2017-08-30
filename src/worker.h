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
        signalProgressChanged(QJsonArray);

    public slots:
        void onStartWorker();
        void onStopWorker();
        void onStartTasks(QList<File>);
        void onStopTasks(QList<File>);
        void onReadyRead();

    public:
        QMap<QString, QProcess> processes;
        QProcess worker;
        bool keepRunning = true;
        WorkerThread();
        ~WorkerThread();
        void run();
        void invoke(QString cmd, QStringList args);
};

#endif // WORKER_H
