#ifndef CONTROL_H
#define CONTROL_H

#include <QString>
#include "gui.h"

class Control {
    public:
        Control();
        ~Control();
        Control(AbstractGUI* gui);
        void startTask(QString url);
}

#endif // CONTROL_H
