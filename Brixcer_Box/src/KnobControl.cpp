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
    // Check if this button was the activated one
    if (!digitalRead(buttonPin)) {
        Serial.println(millis() - buttonReadTime);
        Serial.println("Button");
        buttonReadTime = millis();
        count += 1;
        Serial.println(count);
        return 1;
    }

    return 0;
}
