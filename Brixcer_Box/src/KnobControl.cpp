#include <Arduino.h>
#include "KnobControl.h"


KnobControl::KnobControl(int knobPin, int buttonPin) {
    this->knobPin = knobPin;
    this->buttonPin = buttonPin;
}

int KnobControl::readKnobValue() {
    return digitalRead(knobPin);
}

int KnobControl::readButtonValue() {
    return digitalRead(buttonPin);
}
