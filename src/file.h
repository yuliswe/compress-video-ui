#ifndef FILE_H
#define FILE_H

#include <QString>
#include <QVariant>
#include <QByteArray>
#include <QUrl>

using namespace std;

enum FileStatus {
    ToBeAdded,
    InQueue,
    InProgress,
    Done,
    UserStopped,
    Error
};

enum FileStandard {
    Bilibili
};

class File {
    public:
        QString url = "";
        QString name = "";
        unsigned size = 0;
        FileStatus status;
        QString standard;
        double progress = 0;
        File();
        File(QString url, QString fileStandard, FileStatus status);
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
