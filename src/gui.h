#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QCursor>
#include "file.h"

class AbstractGUI : public QObject {
        Q_OBJECT

    signals:
        void signalDataChanged(QVariant data);

    protected:
        QApplication* app;
        FileList currentTasksModel;
        FileList historyTasksModel;

    public slots:
        virtual void onDeleteCurrentTask(QString url) = 0;

    public:
        int start(int argc, char** argv);
        QVariant getQMLData();
        void notifyDataChanges();
        AbstractGUI();
        virtual ~AbstractGUI();
};


class GUI : public AbstractGUI {
        Q_OBJECT

    public slots:
//        void setMouseCursor(int type);
        virtual void onDeleteCurrentTask(QString url);
};

