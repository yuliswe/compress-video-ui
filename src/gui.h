#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QCursor>

class GUI : public QObject {

    Q_OBJECT

    private: QApplication* app;

    public: GUI();
    public: ~GUI();

    public: int start(int argc, char** argv);

    public slots: void setMouseCursor(int type);
};
