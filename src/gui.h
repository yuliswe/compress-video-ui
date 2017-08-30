#ifndef GUI_H
#define GUI_H

#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QCursor>
#include <QJsonObject>
#include <QSemaphore>
#include "file.h"
#include "worker.h"

class GUI : public QObject {
        Q_OBJECT

//    signals:
//        void signalQMLDataChanged(QVariant data);

    public:
        GUI(int argc, char** argv);
        WorkerThread workerThread;
        virtual ~GUI();

    public slots:
        virtual void onAboutToQuit();
};

#endif
