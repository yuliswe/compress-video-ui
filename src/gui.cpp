#include "gui.h"
#include "file.h"
#include <iostream>
#include <QString>
#include <QDebug>

using namespace std;

int AbstractGUI::start(int argc, char** argv){
    qDebug() << "Application started" << endl;
    this->app = new QApplication(argc, argv);
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
    notifyDataChanges();
    return this->app->exec();
}

AbstractGUI::AbstractGUI() {}
AbstractGUI::~AbstractGUI() {
    delete this->app;
}

QVariant AbstractGUI::getQMLData() {
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

void AbstractGUI::notifyDataChanges() {
    emit this->signalDataChanged(this->getQMLData());
}

//void AbstractGUI::setMouseCursor(int type) {
//    this->app->setOverrideCursor(QCursor(static_cast<Qt::CursorShape>(type)));
//}

void AbstractGUI::onDeleteCurrentTask(QString url) {
    qDebug() << "C++ deletes currentTask url" << url << endl;
}

void AbstractGUI::onAddNewTasks(QVariant urls) {
    QList<QUrl> urlList = urls.value<QList<QUrl>>();
    FileList newFileList;
    for (auto url : urlList) {
        File f(url.toLocalFile(), FileStatus::ToBeAdded);
        newFileList.push_back(f);
    }
    this->newTasksModel.append(newFileList);
    this->notifyDataChanges();
}

void AbstractGUI::onMoveNewTasksToCurrent() {
    for (QList<File>::iterator task = this->newTasksModel.begin();
         task != this->newTasksModel.end();
         task++) {
        task->status = FileStatus::InQueue;
    }
    this->currentTasksModel.append(this->newTasksModel);
    this->newTasksModel.clear();
    this->notifyDataChanges();
}
