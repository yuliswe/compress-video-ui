#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QGraphicsOpacityEffect>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QGraphicsOpacityEffect * effect = new QGraphicsOpacityEffect();
    effect->setOpacity(0.2);
    ui->dragHint->setGraphicsEffect(effect);
}

MainWindow::~MainWindow()
{
    delete ui->dragHint->graphicsEffect();
    delete ui;
}
