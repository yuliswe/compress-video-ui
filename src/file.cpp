#include "file.h"
#include <QString>
#include <iostream>
#include <ostream>
#include <QJsonDocument>
#include <QDebug>
#include <QJsonObject>
#include <QJsonValue>
#include <QFile>

using namespace std;

File::File() {}
File::File(QString url, FileStatus status) {
    this->url = url;
    this->status = status;
    QFile tmp(url);
//    tmp.open(QIODevice::ReadOnly);
//    qDebug() << "open" << url << "exists?" << tmp.exists() << endl;
    this->size = tmp.size();
    qDebug() << tmp.size() << this->size << endl;
}
File::~File() {}
File File::fromQVariant(QVariant v) {
    QJsonValue obj = v.toJsonValue();
    qDebug() << "File:toJsonObject => " << obj << endl;
    File file;
    //    file.name = obj.find("fileUrl").value().toString();
    //    file.size = obj.find("fileSize").value().toInt();
    //    file.status = obj.find("fileStatus").value().toInt();
    //    file.progress = obj.find("progress").value().toDouble();
    //    qDebug() << "File:file => " << obj.find("fileUrl").value() << endl;
    return file;
}

QVariant File::toQVariant() const {
    QVariantMap m;
    m.insert("fileUrl", this->url);
    m.insert("fileSize", this->size);
    m.insert("fileStatus", static_cast<int>(this->status));
    m.insert("percentage", this->progress);
    return m;
}

QByteArray File::toJSON() const {
    this->toQVariant().toJsonDocument().toJson();
}

QDebug operator<<(QDebug o, const File f) {
    o << f.toJSON() << endl;
    return o;
}

//QList<File> FileList::fromQVariant(QVariant v) {
//    QVariantList ls = v.toList();
//    qDebug() << "list" << ls << endl;
//    QList<File> filelist;
//    for (auto i : ls) {
//        qDebug() << i << endl;
//        File f = File::fromQVariant(i);
//        qDebug() << f << endl;
//        filelist.push_back(f);
//    }
//    return filelist;
//}


QVariant FileList::toQVariant() {
    QVariantList filelist;
    for (auto i = this->begin(); i != this->end(); i++) {
        filelist.push_back(i->toQVariant());
    }
    return QVariant(filelist);
}


QDebug operator<<(QDebug o, QList<File> ls) {
    o << ls[0].toQVariant().toJsonDocument().toJson() << endl;
    return o;
}

//FileList::FileList() {}
//FileList::~FileList() {}

//FileList::FileList(QList<File> ls) {
//    this->append(ls);
//}
