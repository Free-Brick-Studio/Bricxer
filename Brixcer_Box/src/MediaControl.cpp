#include <Arduino.h>
#include "MediaControl.h"


MediaControl::MediaControl(int playPausePin, int previousPin, int nextPin) {
    this->togglePlayPausePin = playPausePin;
    this->previousPin = previousPin;
    this->nextPin = nextPin;
}

int* MediaControl::readButtonValues() {
    int buttonValues[] = {digitalRead(togglePlayPausePin), digitalRead(previousPin), digitalRead(nextPin)};
    return buttonValues;
}