Release:DESTDIR = ../release
Release:OBJECTS_DIR = ../release/.obj
Release:MOC_DIR = ../release/.moc
Release:RCC_DIR = ../release/.rcc
Release:UI_DIR = ../release/.ui

Debug:DESTDIR = ../debug
Debug:OBJECTS_DIR = ../debug/.obj
Debug:MOC_DIR = ../debug/.moc
Debug:RCC_DIR = ../debug/.rcc
Debug:UI_DIR = ../debug/.ui

CONFIG += qt
QT += widgets qml
SOURCES = \
    main.cpp \
    gui.cpp \
    file.cpp \
    worker.cpp

HEADERS = \
    gui.h \
    file.h \
    worker.h

RESOURCES = main.qrc
