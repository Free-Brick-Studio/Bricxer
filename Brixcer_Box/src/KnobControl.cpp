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

int CW_ROT  = 0x10;
int CCW_ROT = 0xFFF0;

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

    this->state = START;
}

int KnobControl::readKnobValues() {
    // Grab state of input pins.
    int pinstate = (digitalRead(knobPinB) << 1) | digitalRead(knobPinA);

    // Determine new state from the pins and state table.
    state = transitions[state & 0x7][pinstate];

    // Return emit bits, ie the generated event.
    return state >> 4;
}

int KnobControl::readButtonValue() {
    // Check if this button was the activated one
    if (!digitalRead(buttonPin)) {
        return 1;
    }

    return 0;
}
