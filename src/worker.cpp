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
    Q_ASSERT(getenv("bin_compress_video_worker"));
    QObject::connect(this, signalStopTasks, this, onStopTasks);
    this->worker.setProcessChannelMode(QProcess::ForwardedErrorChannel);
    this->worker.start(QString(getenv("bin_compress_video_worker")));
    QObject::connect(&this->worker, QProcess::readyRead, this, WorkerThread::onReadyRead);
    this->worker.waitForStarted();
    qDebug() << "Started" << getenv("bin_compress_video_worker") << endl;
}
WorkerThread::~WorkerThread() {
}

void WorkerThread::onReadyRead() {
    QByteArray bt = this->worker.readLine();
    QJsonDocument doc = QJsonDocument::fromJson(bt);
    QJsonArray arr = doc.array();
    qDebug() << arr << endl;
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        for (QJsonArray::iterator newData = arr.begin();
             newData != arr.end();
             newData++) {
            QJsonObject obj = newData->toObject();
            QString url = obj["url"].toString();
            QString standard = obj["standard"].toString();
            if (task->url == url && task->standard == standard) {
                task->status = readFileStatus(obj["status"].toString());
                task->progress = obj["percentage"].toDouble();
            }
        }
    }
    emit this->notifyDataChanges();
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
    emit this->signalQMLDataChanged(this->getQMLData());
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
    this->notifyDataChanges();
}

void WorkerThread::onAddNewTasks(QVariant urls, QString standard) {
    QList<QUrl> urlList = urls.value<QList<QUrl>>();
    FileList newFileList;
    for (auto url : urlList) {
        File f(url.toLocalFile(), standard, FileStatus::ToBeAdded);
        newFileList.push_back(f);
    }
    this->newTasksModel.append(newFileList);
    this->notifyDataChanges();
}

void WorkerThread::onMoveNewTasksToCurrent() {
    for (QList<File>::iterator task = this->newTasksModel.begin();
         task != this->newTasksModel.end();
         task++) {
        task->status = FileStatus::InQueue;
    }
    this->currentTasksModel.append(this->newTasksModel);
    this->newTasksModel.clear();
    this->notifyDataChanges();
}


void WorkerThread::onStartCurrentTasks() {
    qDebug() << "onStartCurrentTasks" << endl;
    emit this->signalStartTasks(this->currentTasksModel);
    this->notifyDataChanges();
}


void WorkerThread::onStopCurrentTasks() {
    qDebug() << "onStopCurrentTasks" << endl;
    emit this->signalStopTasks(this->currentTasksModel);
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        task->status = FileStatus::UserStopped;
    }
    this->notifyDataChanges();
}
