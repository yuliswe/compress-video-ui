#include "gui.h"
#include "file.h"
#include <iostream>
#include <QString>
#include <QDebug>
#include <QJsonObject>
#include <QJsonArray>

using namespace std;

GUI::GUI(int argc, char** argv) {
    qDebug() << "Application started" << endl;
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("cpp", this);
    engine.load(QUrl("qrc:/qml/main.qml"));
    QObject* qml = engine.rootObjects().first();
    QObject::connect(qml, SIGNAL(signalRemoveCurrentTask(QString, QString)),
                     this, SLOT(onRemoveCurrentTask(QString, QString)));
    QObject::connect(qml, SIGNAL(signalMoveNewTasksToCurrent()),
                     this, SLOT(onMoveNewTasksToCurrent()));
    QObject::connect(qml, SIGNAL(signalAddNewTasks(QVariant, QString)),
                     this, SLOT(onAddNewTasks(QVariant, QString)));
    QObject::connect(qml, SIGNAL(signalStartCurrentTasks()),
                     this, SLOT(onStartCurrentTasks()));
    QObject::connect(qml, SIGNAL(signalStopCurrentTasks()),
                     this, SLOT(onStopCurrentTasks()));
    QObject::connect(&this->workerThread, WorkerThread::signalProgressChanged,
                     this, GUI::onProgressChanged);
    emit this->workerThread.signalStartWorker();
    this->notifyDataChanges();
    QObject::connect(&app, SIGNAL(aboutToQuit()),
                     this, SLOT(onAboutToQuit()));
    app.exec();
}

GUI::~GUI() {}

void GUI::onAboutToQuit() {
    emit this->workerThread.signalStopWorker();
}

FileStatus readFileStatus(QString fs) {
    FileStatus s;
    if (fs == "InQueue") {
        s = FileStatus::InQueue;
    } else if (fs == "InProgress") {
        s = FileStatus::InProgress;
    } else if (fs == "Done") {
        s = FileStatus::Done;
    } else if (fs == "Error") {
        s = FileStatus::Error;
    } else if (fs == "UserStopped") {
        s = FileStatus::UserStopped;
    } else {
        s = FileStatus::Error;
    }
    return s;
}

void GUI::onProgressChanged(QJsonArray obj) {
    qDebug() << obj << endl;
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        for (QJsonArray::iterator newData = obj.begin();
             newData != obj.end();
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

QVariant GUI::getQMLData() {
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

void GUI::notifyDataChanges() {
    emit this->signalDataChanged(this->getQMLData());
}

//void GUI::setMouseCursor(int type) {
//    this->app->setOverrideCursor(QCursor(static_cast<Qt::CursorShape>(type)));
//}

void GUI::onRemoveCurrentTask(QString url, QString standard) {
    QList<File> args;
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        if (url == task->url && task->standard == standard) {
            args << *task;
            this->currentTasksModel.erase(task);
        }
    }
    emit this->workerThread.signalStopTasks(args);
    this->notifyDataChanges();
}

void GUI::onAddNewTasks(QVariant urls, QString standard) {
    QList<QUrl> urlList = urls.value<QList<QUrl>>();
    FileList newFileList;
    for (auto url : urlList) {
        File f(url.toLocalFile(), standard, FileStatus::ToBeAdded);
        newFileList.push_back(f);
    }
    this->newTasksModel.append(newFileList);
    this->notifyDataChanges();
}

void GUI::onMoveNewTasksToCurrent() {
    for (QList<File>::iterator task = this->newTasksModel.begin();
         task != this->newTasksModel.end();
         task++) {
        task->status = FileStatus::InQueue;
    }
    this->currentTasksModel.append(this->newTasksModel);
    this->newTasksModel.clear();
    this->notifyDataChanges();
}


void GUI::onStartCurrentTasks() {
    qDebug() << "onStartCurrentTasks" << endl;
    emit this->workerThread.signalStartTasks(this->currentTasksModel);
    this->notifyDataChanges();
}


void GUI::onStopCurrentTasks() {
    qDebug() << "onStopCurrentTasks" << endl;
    emit this->workerThread.signalStopTasks(this->currentTasksModel);
    for (QList<File>::iterator task = this->currentTasksModel.begin();
         task != this->currentTasksModel.end();
         task++) {
        task->status = FileStatus::UserStopped;
    }
    this->notifyDataChanges();
}
