#include <Arduino.h>
#include "KnobControl.h"
#include "LedControl.h"
#include "MediaControl.h"

#define Knob5OutA D1
#define Knob5OutB D0
// GND
// GND
#define Knob1OutA D2
#define Knob1OutB D3
#define Knob2OutA D4
#define Knob2OutB D12
#define Knob3OutA D6
#define Knob3OutB D7
#define Knob4OutA D8
#define Knob4OutB D9


#define PlayPause RXLED0
// GND
// RST
// VCC
#define Previous D21
#define Next D20
#define Button5 D19
#define Button4 D18
#define Button3 D15
#define Button2 D14
#define Button1 D16
#define LedChain D10

#define KnobCount 5

#define LEDPIN 13

// Define controls for the box
KnobControl knobs[KnobCount];
LedControl leds[KnobCount];
MediaControl mediaControl(PlayPause, Previous, Next);


void setup() {
    // Turn on the serial monitor
    //Serial.begin(9600);

    pinMode(LEDPIN, OUTPUT);

    int knobPins[] = {Knob1OutA, Knob1OutB, Knob2OutA, Knob2OutB, Knob3OutA, Knob3OutB, Knob4OutA, Knob4OutB, Knob5OutA, Knob5OutB};
    int buttonPins[] = {Button1, Button2, Button3, Button4, Button5};

    // Create the controllers for the knobs and leds
    for (int i = 0; i < KnobCount; i++) {
        KnobControl knob(knobPins[i * 2], knobPins[i * 2 + 1], buttonPins[i]);
        knobs[i] = knob;

        LedControl led(LedChain);
        leds[i] = led;
    }
}
 
void loop() {
    //Serial.printLn("0.Value.");
    digitalWrite(LEDPIN, HIGH);
    delay(1000);
    digitalWrite(LEDPIN, LOW);
    delay(1000);
}

void sendData(int control, int action, int value) {

}

void receiveData() {

}
