#include "worker.h"
#include "gui.h"
#include <QThread>
#include <QProcess>
#include <QStringList>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>

void WorkerThread::run() {
    //    while(this->keepRunning) {
    //        qDebug() << " working..." << endl;
    ////        for (auto i = this->processes.begin();
    ////             i != this->processes.end();
    ////             i++) {
    ////            i->
    ////        }
    //        this->sleep(1);
    //    }
}

WorkerThread::WorkerThread() {
    QObject::connect(this, stopLoop, this, onStopLoop);
    QObject::connect(this, startLoop, this, onStartLoop);
    QObject::connect(this, startTasks, this, onStartTasks);
    this->worker.start();
}
WorkerThread::~WorkerThread() {}

void WorkerThread::onStopLoop() {
    this->keepRunning = false;
}

void WorkerThread::onStartLoop() {
    this->keepRunning = true;
    this->start();
}

void WorkerThread::onStartTasks(QStringList urls) {
    qDebug() << "start " << urls << endl;
    this->invoke("startTask", urls);
}

void WorkerThread::invoke(QString cmd, QStringList args) {
    QJsonObject obj;
    obj.insert("cmd", cmd);
    QJsonArray arr;
    for (QString s : args) {
        arr.push_back(s);
    }
    obj.insert("args", arr);
    QJsonDocument doc(obj);
    qDebug() << doc.toJson(QJsonDocument::JsonFormat::Compact) << endl;
    this->worker.write(doc.toJson(QJsonDocument::JsonFormat::Compact));
}
