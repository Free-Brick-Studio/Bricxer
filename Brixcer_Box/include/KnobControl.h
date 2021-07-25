class KnobControl {

    int knobPinA;
    int knobPinB;
    int buttonPin;

    int prevPinARead;
    int prevPinBRead;

    public:
        KnobControl(int knobPinA, int knobPinB, int buttonPin);
        int readKnobValues();
        int readButtonValue();
};
