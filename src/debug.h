#ifndef DEBUG_H
#define DEBUG_H

#include <QDebug>

class Debug : public QDebug {
        QDebug operator<<(const File f) {
            o << f.toJSON() << endl;
            return o;
        }
}

#endif // DEBUG_H
