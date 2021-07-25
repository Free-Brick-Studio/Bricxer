#include <Adafruit_NeoPixel.h>

class LedControl {

    // Number of LEDs per ring
    static const int LEDS_PER_RING = 12;

    // Number of LEDs dedicated to application color
    static const int APPLICATION_LEDS = 3;

    // Object for handling ring chain
    static Adafruit_NeoPixel strip;

    int ringNum;

    public:
        static void InitLedControl(int count, int pin);

        LedControl(int ringNum);
        void setVolume(int volume);
        void setColorMatrix(int* matrix);
};
