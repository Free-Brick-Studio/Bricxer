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

    int temp = 0;
    if (prevPinARead != knobValues[0] || prevPinBRead != knobValues[1]) {
        Serial.print(knobValues[0]);
        Serial.println(knobValues[1]);

        bool aChanged = prevPinARead != knobValues[0];
        // bool bChanged = prevPinBRead != knobValues[1];
        bool pinsAreEqual = knobValues[0] == knobValues[1];

        if (aChanged && pinsAreEqual) {
            temp = -1;
        }
        if (aChanged && !pinsAreEqual) {
            temp = 1;
        }

        // if (bChanged && pinsAreEqual) {
        //     temp = 1;
        // }
        // if (bChanged && !pinsAreEqual) {
        //     temp = -1;
        // }
        // if (aChanged && bChanged) {
        //     temp = 2;
        // }

        prevPinARead = knobValues[0];
        prevPinBRead = knobValues[1];
    }

    return temp;
}

int KnobControl::readKnobAValue() {
    int curr = digitalRead(knobPinA);

    int temp = 0;
    if (prevPinARead != curr) {
        if (curr != digitalRead(knobPinB)) {
            temp = 1;
        } else {
            temp = -1;
        }

        prevPinARead = curr;
    }

    return temp;
}

void KnobControl::readKnobBValue() {
    prevPinBRead = !prevPinBRead;
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
