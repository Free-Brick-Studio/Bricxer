#include <Arduino.h>
#include "MediaControl.h"


MediaControl::MediaControl(int playPausePin, int previousPin, int nextPin) {
    this->togglePlayPausePin = playPausePin;
    this->previousPin = previousPin;
    this->nextPin = nextPin;

    pinMode(this->togglePlayPausePin, INPUT);
    pinMode(this->previousPin, INPUT);
    pinMode(this->nextPin, INPUT);
}

int* MediaControl::readButtonValues() {
    int buttonValues[] = {digitalRead(togglePlayPausePin), digitalRead(previousPin), digitalRead(nextPin)};
    return buttonValues;
}
