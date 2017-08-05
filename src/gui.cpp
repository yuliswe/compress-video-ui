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
    QVariantMap m;
    m.insert("currentTasksModel", cur);
    m.insert("historyTasksModel", his);
    return m;
}

void AbstractGUI::notifyDataChanges() {
    emit this->signalDataChanged(this->getQMLData());
}

//void AbstractGUI::setMouseCursor(int type) {
//    this->app->setOverrideCursor(QCursor(static_cast<Qt::CursorShape>(type)));
//}

void GUI::onDeleteCurrentTask(QString url) {
    qDebug() << "C++ deletes currentTask url" << url << endl;
}
