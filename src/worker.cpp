#include "worker.h"
#include "gui.h"
#include <QThread>
#include <QProcess>
#include <QStringList>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <cstdlib>

using namespace std;

void WorkerThread::run() {
    //        while(this->keepRunning) {
    //            qDebug() << " working..." << endl;
    //    //        for (auto i = this->processes.begin();
    //    //             i != this->processes.end();
    //    //             i++) {
    //    //            i->
    //    //        }
    //            this->sleep(1);
    //            qDebug() << this->worker.readAllStandardError() << endl;
    //            qDebug() << this->worker.readAllStandardOutput() << endl;
    //        }
}

WorkerThread::WorkerThread() {
    QObject::connect(this, signalStopWorker, this, onStopWorker);
    QObject::connect(this, signalStartWorker, this, onStartWorker);
    QObject::connect(this, signalStartTasks, this, onStartTasks);
    QObject::connect(this, signalStopTasks, this, onStopTasks);
    qDebug() << "Started " << getenv("bin_compress_video_worker") << endl;
    this->worker.setProcessChannelMode(QProcess::ForwardedErrorChannel);
    this->worker.start(QString(getenv("bin_compress_video_worker")));
    QObject::connect(&this->worker, QProcess::readyRead, this, WorkerThread::onReadyRead);
    this->worker.waitForStarted();
}
WorkerThread::~WorkerThread() {
}

void WorkerThread::onReadyRead() {
    QByteArray bt = this->worker.readLine();
    QJsonDocument doc = QJsonDocument::fromJson(bt);
    QJsonArray arr = doc.array();
    emit this->signalProgressChanged(arr);
}

void WorkerThread::onStopWorker() {
    this->keepRunning = false;
    this->invoke("quit", QStringList());
    this->worker.waitForFinished(-1);
}

void WorkerThread::onStartWorker() {
    this->keepRunning = true;
    this->start();
}

void WorkerThread::onStartTasks(QList<File> files) {
    for (auto f : files) {
        QStringList ls;
        ls << f.url << f.standard;
        this->invoke("startTask", ls);
    }
}

void WorkerThread::onStopTasks(QList<File> files) {
    for (auto f : files) {
        QStringList args;
        args << f.url << f.standard;
        this->invoke("stopTask", args);
    }
}

void WorkerThread::invoke(QString cmd, QStringList args) {
    QJsonObject obj;
    obj.insert("command", cmd);
    QJsonArray arr;
    for (QString s : args) {
        arr.push_back(s);
    }
    obj.insert("arguments", arr);
    QJsonDocument doc(obj);
    qDebug() << doc << endl;
    qDebug() << doc.toJson(QJsonDocument::JsonFormat::Compact) << endl;
    this->worker.write(doc.toJson(QJsonDocument::JsonFormat::Compact));
    this->worker.write("\n");
    this->worker.waitForBytesWritten();
}
