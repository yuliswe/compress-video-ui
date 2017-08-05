#ifndef FILE_H
#define FILE_H

#include <QString>
#include <QVariant>
#include <QByteArray>

using namespace std;

class File {
    public:
        QString name;
        QString size;
        QString status;
        double progress;
        File();
        ~File();
        static File fromQVariant(QVariant);
        QVariant toQVariant() const;
        QByteArray toJSON() const;
};

QDebug operator<<(QDebug o, const File f);

class FileList : public QList<File> {
    public:
//        FileList();
//        virtual ~FileList();
//        static FileList fromQVariant(QVariant);
        virtual QVariant toQVariant();
};

#endif // FILE_H
