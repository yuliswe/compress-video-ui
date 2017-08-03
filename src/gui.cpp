#include "gui.h"
#include <iostream>

using namespace std;

GUI::GUI() {};
GUI::~GUI() {
    delete this->app;
};

int GUI::start(int argc, char** argv){
    this->app = new QApplication(argc, argv);
    QQmlApplicationEngine engine;
    engine.load(QUrl("qrc:/qml/main.qml"));
    QObject* root = engine.rootObjects().first();
    // QObject::connect(root, SIGNAL(setMouseCursor(int)),
                    //  this, SLOT(setMouseCursor(int)));
    return this->app->exec();
};

void GUI::setMouseCursor(int type) {
    this->app->setOverrideCursor(QCursor(static_cast<Qt::CursorShape>(type)));
}
