#include <Arduino.h>
#include "LedControl.h"


Adafruit_NeoPixel LedControl::strip;

LedControl::LedControl(int ringNum) {
    this->ringNum = ringNum;
}

void LedControl::InitLedControl(int count, int pin) {
    // Parameter 1 = number of pixels in strip
    // Parameter 2 = pin number (most are valid)
    // Parameter 3 = pixel type flags, add together as needed:
    //   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
    //   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
    //   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
    //   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
    LedControl::strip = Adafruit_NeoPixel(LEDS_PER_RING * count, pin, NEO_GRB + NEO_KHZ800);

    strip.begin();
    strip.setBrightness(1);
    strip.show();
}

void LedControl::setVolume(int volume) {
    int volumeStartLed = this->ringNum * LEDS_PER_RING + APPLICATION_LEDS;
    int volumeLedRange = LEDS_PER_RING - APPLICATION_LEDS;
    int pixel = map(volume, 0, 100, 0, volumeLedRange - 1);

    strip.fill(strip.Color(0, 0, 0), volumeStartLed, volumeLedRange);
    strip.setPixelColor(volumeStartLed + pixel, strip.Color(0, 255, 0));
    strip.show();
}

void LedControl::setColorMatrix(int* matrix) {
    strip.fill(strip.Color(matrix[0], matrix[1], matrix[2]), this->ringNum * LEDS_PER_RING, APPLICATION_LEDS);
    strip.show();
}
