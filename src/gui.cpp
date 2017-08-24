#include "gui.h"
#include "file.h"
#include <iostream>
#include <QString>
#include <QDebug>

using namespace std;

GUI::GUI(int argc, char** argv) {
    qDebug() << "Application started" << endl;
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("cpp", this);
    engine.load(QUrl("qrc:/qml/main.qml"));
    QObject* qml = engine.rootObjects().first();
    QObject::connect(qml, SIGNAL(signalDeleteCurrentTask(QString)),
                     this, SLOT(onDeleteCurrentTask(QString)));
    QObject::connect(qml, SIGNAL(signalMoveNewTasksToCurrent()),
                     this, SLOT(onMoveNewTasksToCurrent()));
    QObject::connect(qml, SIGNAL(signalAddNewTasks(QVariant)),
                     this, SLOT(onAddNewTasks(QVariant)));
    QObject::connect(qml, SIGNAL(signalStartCurrentTasks()),
                     this, SLOT(onStartCurrentTasks()));
    emit this->workerThread.start();
    notifyDataChanges();
    app.exec();
}

GUI::~GUI() {
    emit this->workerThread.quit();
    this->workerThread.wait();
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

void GUI::onDeleteCurrentTask(QString url) {
    qDebug() << "C++ deletes currentTask url" << url << endl;
}

void GUI::onAddNewTasks(QVariant urls) {
    QList<QUrl> urlList = urls.value<QList<QUrl>>();
    FileList newFileList;
    for (auto url : urlList) {
        File f(url.toLocalFile(), FileStatus::ToBeAdded);
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
    QString a = "dummy";
    QList<QString> ls;
    ls.push_back(a);
    emit this->workerThread.startTasks(ls);
//    if (this->workerThread.isRunning()) {
//        qDebug() << "Worker is already running" << endl;
//        return;
//    }
//    for (QList<File>::iterator task = this->currentTasksModel.begin();
//         task != this->currentTasksModel.end();
//         task++) {
//        task->status = FileStatus::InProgess;
//    }
    this->notifyDataChanges();
}


void GUI::onStopCurrentTasks() {
}
