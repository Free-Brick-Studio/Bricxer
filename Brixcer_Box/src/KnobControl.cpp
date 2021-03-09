#include <Arduino.h>
#include "KnobControl.h"


KnobControl::KnobControl(int knobPinA, int knobPinB, int buttonPin) {
    this->knobPinA = knobPinA;
    this->knobPinB = knobPinB;
    this->buttonPin = buttonPin;

    pinMode(this->knobPinA, INPUT_PULLUP);
    pinMode(this->knobPinB, INPUT_PULLUP);
    pinMode(this->buttonPin, INPUT_PULLUP);
}

int* KnobControl::readKnobValues() {
    int knobValues[] = {digitalRead(knobPinA), digitalRead(knobPinB)};
    return knobValues;
}

int KnobControl::readButtonValue() {
    return !digitalRead(buttonPin);
}
