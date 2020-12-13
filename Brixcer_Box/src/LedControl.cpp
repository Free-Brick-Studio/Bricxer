#include <Arduino.h>
#include "LedControl.h"


LedControl::LedControl(int ledPin) {
    this->ledPin = ledPin;

    pinMode(this->ledPin, OUTPUT);
}

void LedControl::setVolume(int volume) {
    this->volume = volume;
}

void LedControl::setColorMatrix(int* matrix) {
    for (int i = 0; i < COLORS; i++) {
        this->color_matrix[i] = matrix[i];
    }
}
