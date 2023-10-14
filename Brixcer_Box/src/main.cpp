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

// Define controls for the box
KnobControl* knobs = (KnobControl*) malloc(sizeof(KnobControl) * KnobCount);
LedControl* leds = (LedControl*) malloc(sizeof(LedControl) * KnobCount);
//MediaControl mediaControl(PlayPause, Previous, Next);

// Define array for Serial input
const int numChars = 33; // 32 chars + 1 for \0
char receivedChars[numChars];

// Define Serial interface
void receiveData();
void sendData(int, int, int);

// Define rotary encoder interface
void buttonClick();
void knobPinTrigger();

void setup() {
    // Turn on the serial monitor
    Serial.begin(9600);

    int knobPins[] = {Knob1OutA, Knob1OutB, Knob2OutA, Knob2OutB, Knob3OutA, Knob3OutB, Knob4OutA, Knob4OutB, Knob5OutA, Knob5OutB};
    int buttonPins[] = {Button1, Button2, Button3, Button4, Button5};

    LedControl::InitLedControl(KnobCount, LedChain);

    // Create the controllers for the knobs and leds
    for (int i = 0; i < KnobCount; i++) {
        KnobControl knob(knobPins[i * 2], knobPins[i * 2 + 1], buttonPins[i]);
        knobs[i] = knob;

        attachInterrupt(buttonPins[i], buttonClick, FALLING);

        LedControl led(i);
        leds[i] = led;
    }
}

void loop() {
    if (Serial.available() > 0) {
        receiveData();
    }

    knobPinTrigger();
}

int countDigits(int num) {
    int digits = 0;

    while (num) {
        num /= 10;
        digits++;
    }

    return digits;
}

void sendData(int control, int action, int value) {
    // Create buffer for the control.action.value combo (two additional spots for \n and \0)
    char str[countDigits(control) + countDigits(action) + countDigits(value) + 4];
    sprintf(str, "%d.%d.%d\n", control, action, value);
    Serial.print(str);
}

void parseData(char* changedValue) {
    char* index;

    index = strtok(changedValue, ".");
    int control = atoi(index);
 
    index = strtok(NULL, ".");
    int action = atoi(index);

    if (action == 0) {
        index = strtok(NULL, ".");
        int volume = atoi(index);

        if (volume < 0) {
            volume = 0;
        } else if (volume > 100) {
            volume = 100;
        }

        leds[control].setVolume(volume);
    } else if (action == 1) {
        index = strtok(NULL, "[,");
        int r = atoi(index);

        index = strtok(NULL, ",");
        int g = atoi(index);

        index = strtok(NULL, ",]");
        int b = atoi(index);

        // Serial.print("IColors: "); Serial.print(r); Serial.print(" "); Serial.print(g); Serial.print(" "); Serial.println(b);
        int colors[3] = {r, g, b};
        leds[control].setColorMatrix(colors);
    }
}

void receiveData() {
    int i = 0;
    char data;

    // Ignore excess data > numChars
    while (Serial.available() > 0 && i < numChars) {
        data = Serial.read();

        receivedChars[i++] = data;
    }
    receivedChars[i] = '\0';

    // Serial.print("I received: ");
    // Serial.println(receivedChars);

    parseData(receivedChars);
}

void buttonClick() {
    for (int i = 0; i < KnobCount; i++) {
        int value = knobs[i].readButtonValue();
        if (value) {
            sendData(i, 0, value);
        }
    }
}

void knobPinTrigger() {
    for (int i = 0; i < KnobCount; i++) {
        int value = knobs[i].getNumberOfRotations();
        if (value != 0) {
            sendData(i, 0, value);
        }
    }
}
