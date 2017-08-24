#ifndef WORKER_H
#define WORKER_H

#include <QThread>
#include <QDebug>
#include <QProcess>
#include <QStringList>

class WorkerThread : public QThread {
        Q_OBJECT
    signals:
        startLoop();
        stopLoop();
        startTasks(QStringList);

    public slots:
        void onStartLoop();
        void onStopLoop();
        void onStartTasks(QStringList);

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
