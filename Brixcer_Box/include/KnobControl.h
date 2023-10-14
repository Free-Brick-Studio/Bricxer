class KnobControl {

    // Interval of time to count the number of rotations
    static const int ROTATION_COUNT_INTERVAL_MS = 200;

    int knobPinA;
    int knobPinB;
    int buttonPin;

    int state;

    int rotationCounter;
    unsigned long timeOfLastUpdate;

    public:
        KnobControl(int knobPinA, int knobPinB, int buttonPin);
        int readKnobValues();
        int getNumberOfRotations();
        int readButtonValue();
};
