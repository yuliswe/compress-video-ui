#include "worker.h"
#include "gui.h"
#include <QThread>
#include <QProcess>
#include <QStringList>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <cstdlib>
#include <QtGlobal>
#include <cstdlib>
using namespace std;

void WorkerThread::run() {
    while(this->keepRunning) {
        this->msleep(50);
        emit this->signalWorkerInvoke("report", QStringList());
        this->worker.waitForReadyRead();
    }
}

WorkerThread::WorkerThread() {
    QObject::connect(this, &WorkerThread::signalStopWorker, this, &WorkerThread::onStopWorker);
    QObject::connect(this, &WorkerThread::signalStartWorker, this, &WorkerThread::onStartWorker);
    QObject::connect(this, &WorkerThread::signalStartTasks, this, &WorkerThread::onStartTasks);
    QObject::connect(this, &WorkerThread::signalWorkerInvoke, this, &WorkerThread::onWorkerInvoke);
    QObject::connect(this, &WorkerThread::signalStopTasks, this, &WorkerThread::onStopTasks);
    this->worker.setProcessChannelMode(QProcess::ForwardedErrorChannel);
    QString bin = getenv("compress_video_bin");
    this->worker.start(bin + QString("/compress-video-worker"));
    QObject::connect(&this->worker, &QProcess::readyRead, this, &WorkerThread::onReadyRead);
    this->worker.waitForStarted();
}

WorkerThread::~WorkerThread() {
    this->wait();
}

void WorkerThread::onReadyRead() {
    QByteArray bt;
    while (this->worker.bytesAvailable() > 0) {
        bt = this->worker.readLine();
    }
    QJsonDocument doc = QJsonDocument::fromJson(bt);
    QJsonArray arr = doc.array();
    emit this->signalQMLDataChanged(doc.toVariant());
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

void WorkerThread::onWorkerInvoke(QString cmd, QVariant args) {
    QStringList ls = args.value<QStringList>();
    this->invoke(cmd, ls);
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

QVariant WorkerThread::getQMLData() {
    QVariant newData;
    QVariant cur = this->currentTasksModel.toQVariant();
    QVariant his = this->historyTasksModel.toQVariant();
    QVariant nts = this->newTasksModel.toQVariant();
    QVariantMap m;
    m.insert("currentTasksModel", cur);
    m.insert("historyTasksModel", his);
    m.insert("newTasksModel", nts);
    return m;
}

void WorkerThread::notifyDataChanges() {
    //    emit this->signalQMLDataChanged(this->getQMLData());
}

void WorkerThread::onRemoveCurrentTask(QString url, QString standard) {
    QList<File> args;
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        if (url == task->url && task->standard == standard) {
            args << *task;
            this->currentTasksModel.erase(task);
        }
    }
    emit this->signalStopTasks(args);
    //    this->notifyDataChanges();
}

void WorkerThread::onAddNewTasks(QVariant urls, QString standard) {
    QList<QUrl> urlList = urls.value<QList<QUrl>>();
    FileList newFileList;
    for (auto url : urlList) {
        File f(url.toLocalFile(), standard, FileStatus::ToBeAdded);
        newFileList.push_back(f);
    }
    this->newTasksModel.append(newFileList);
    //    this->notifyDataChanges();
}

void WorkerThread::onMoveNewTasksToCurrent() {
    for (QList<File>::iterator task = this->newTasksModel.begin();
         task != this->newTasksModel.end();
         task++) {
        QStringList args;
        args << task->url << task->standard;
        this->invoke("queueTask", args);
    }
    this->newTasksModel.clear();
    //    this->notifyDataChanges();
}


void WorkerThread::onStartCurrentTasks() {
    qDebug() << "onStartCurrentTasks" << endl;
    emit this->signalStartTasks(this->currentTasksModel);
    //    this->notifyDataChanges();
}


void WorkerThread::onStopCurrentTasks() {
    qDebug() << "onStopCurrentTasks" << endl;
    emit this->signalStopTasks(this->currentTasksModel);
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        task->status = FileStatus::UserStopped;
    }
    //    this->notifyDataChanges();
}
