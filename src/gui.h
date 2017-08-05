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
        FileList newTasksModel;

    public:
        int start(int argc, char** argv);
        QVariant getQMLData();
        void notifyDataChanges();
        AbstractGUI();
        virtual ~AbstractGUI();

    public slots:
        virtual void onDeleteCurrentTask(QString url);
        virtual void onMoveNewTasksToCurrent();
        virtual void onAddNewTasks(QVariant urls);
};


class GUI : public AbstractGUI {
        Q_OBJECT

    public slots:
//        void setMouseCursor(int type);
};

