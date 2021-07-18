#include <Arduino.h>
#include <Adafruit_NeoPixel.h>
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
#define LEDS 12

// Define controls for the box
KnobControl* knobs = (KnobControl*) malloc(sizeof(KnobControl) * KnobCount);
//LedControl leds[KnobCount];
//MediaControl mediaControl(PlayPause, Previous, Next);

Adafruit_NeoPixel strip;


void buttonClick();
void knobPinTrigger();
void sendData(int, int, int);
void applicationColor(int);
void applicationVolume();

void setup() {
    // Turn on the serial monitor
    // Serial.begin(9600);

    // int knobPins[] = {Knob1OutA, Knob1OutB, Knob2OutA, Knob2OutB, Knob3OutA, Knob3OutB, Knob4OutA, Knob4OutB, Knob5OutA, Knob5OutB};
    // int buttonPins[] = {Button1, Button2, Button3, Button4, Button5};

    // Parameter 1 = number of pixels in strip
    // Parameter 2 = pin number (most are valid)
    // Parameter 3 = pixel type flags, add together as needed:
    //   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
    //   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
    //   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
    //   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
    strip = Adafruit_NeoPixel(LEDS*KnobCount, 15, NEO_GRB + NEO_KHZ800);
    strip.begin();
    strip.setBrightness(1); //adjust brightness here
    strip.show(); // Initialize all pixels to 'off'

    // Create the controllers for the knobs and leds
    for (int i = 0; i < KnobCount; i++) {
        KnobControl knob(knobPins[i * 2], knobPins[i * 2 + 1], buttonPins[i]);
        // knobs[i] = knob;
        // attachInterrupt(buttonPins[i], buttonClick, FALLING);
        // attachInterrupt(knobPins[i * 2], knobPinTrigger, FALLING);
        // attachInterrupt(knobPins[i * 2 + 1], knobPinTrigger, FALLING);
        applicationColor(i);
    }
}

void loop() {
    applicationVolume();
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

void receiveData() {

}

void buttonClick() {
    for (int i = 0; i < KnobCount; i++) {
        int button = knobs[i].readButtonValue();
        if (button) {
            sendData(i, 0, button);
        }
    }
}

void knobPinTrigger() {
    for (int i = 0; i < KnobCount; i++) {
        int button = knobs[i].readKnobValues();
        if (button != 0) {
            sendData(i, 1, button);
        } 
    }
}

void applicationColor(int ringNum) {
    for(int i = 0; i < LEDS / 3; i++) {
        strip.setPixelColor(ringNum * LEDS + i, strip.Color(0, 0, 255)); 
    }

    strip.show();
}

void applicationVolume() {
    for (int i = LEDS/3; i < LEDS; i++) {
        for (int j = 0; j < KnobCount; j++) {
            strip.setPixelColor(j * LEDS + i, strip.Color(255, 0, 0));

            if (i != LEDS/3) {
                strip.setPixelColor(j * LEDS + i-1, strip.Color(0, 0, 0));
            }
        }

        strip.show();
        delay(100);
    }

    for (int i = LEDS-1; i >= strip.numPixels()/(3*KnobCount); i--) {
        for (int j = 0; j < KnobCount; j++) {
            strip.setPixelColor(j * LEDS + i, strip.Color(255, 0, 0));

            if (i != LEDS-1) {
                strip.setPixelColor(j * LEDS + i+1, strip.Color(0, 0, 0));
            }
        }

        strip.show();
        delay(100);
    }
}
