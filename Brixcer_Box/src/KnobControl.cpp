#include <Arduino.h>
#include "KnobControl.h"


KnobControl::KnobControl(int knobPinA, int knobPinB, int buttonPin) {
    this->knobPinA = knobPinA;
    this->knobPinB = knobPinB;
    this->buttonPin = buttonPin;

    pinMode(this->knobPinA, INPUT);
    pinMode(this->knobPinB, INPUT);
    pinMode(this->buttonPin, INPUT_PULLUP);
}

int KnobControl::readKnobValues() {
    int knobValues[2] = {digitalRead(knobPinA), digitalRead(knobPinB)};

    // Check if this knob was the activated one
    int spinDirection = 0;
    if (prevPinARead != knobValues[0] || prevPinBRead != knobValues[1]) {
        bool aChanged = prevPinARead != knobValues[0];
        bool pinsAreEqual = knobValues[0] == knobValues[1];

        if (aChanged && pinsAreEqual) {
            spinDirection = -1;
        }
        if (aChanged && !pinsAreEqual) {
            spinDirection = 1;
        }

        prevPinARead = knobValues[0];
        prevPinBRead = knobValues[1];
    }

    return spinDirection;
}

int KnobControl::readButtonValue() {
    // Check if this button was the activated one
    if (!digitalRead(buttonPin)) {
        return 1;
    }

    return 0;
}
