#include <Arduino.h>
#include "KnobControl.h"

enum position {
    START     = 0,
    START_CW  = 1,
    START_CCW = 2,
    MID       = 3,
    END_CW    = 4,
    END_CCW   = 5,
};

int16_t CW_ROT  = 0x10;
int16_t CCW_ROT = 0xFFF0;

const int transitions[6][4] = {
    // Starting Position
    { START,   START_CW,  START_CCW, START },
    // First step in CW direction
    { START,   START_CW,  START,     MID },
    // First step in CCW direction
    { START,   START,     START_CCW, MID },
    // Middle Position
    { MID,     END_CCW,   END_CW,    MID },
    // Last step in CW direction
    { CW_ROT,  START,     END_CW,    MID },
    // Last step in CCW direction
    { CCW_ROT, END_CCW,   START,     MID },
};


KnobControl::KnobControl(int knobPinA, int knobPinB, int buttonPin) {
    this->knobPinA = knobPinA;
    this->knobPinB = knobPinB;
    this->buttonPin = buttonPin;

    pinMode(this->knobPinA, INPUT);
    pinMode(this->knobPinB, INPUT);
    pinMode(this->buttonPin, INPUT_PULLUP);

    state = START;
    rotationCounter = 0;
}

int KnobControl::readKnobValues() {
    // Read the current value of the pins
    int pinstate = (digitalRead(knobPinB) << 1) | digitalRead(knobPinA);

    // Determine the current state from the transition table
    state = transitions[state & 0x7][pinstate];

    // Return the direction of rotation (0: rotation hasn't completed, 1: CW, -1: CCW)
    return state >> 4;
}

int KnobControl::getNumberOfRotations() {
    // Get the direction of the latest rotation
    int direction = this->readKnobValues();

    // Add the rotation to the directional rotation count
    rotationCounter += direction;

    // If the counting period has ended, send the current rotation count
    if (millis() - timeOfLastUpdate > ROTATION_COUNT_INTERVAL_MS) {
        // Get the number of directional rotations
        int rotations = rotationCounter;

        // Reset rotation counter
        rotationCounter = 0;
        timeOfLastUpdate = millis();

        return rotations;
    }

    return 0;
}

int KnobControl::readButtonValue() {
    // Check if this button was the activated one
    if (!digitalRead(buttonPin)) {
        return 1;
    }

    return 0;
}
