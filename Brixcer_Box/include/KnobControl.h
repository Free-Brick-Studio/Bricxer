class KnobControl {

    int knobPinA;
    int knobPinB;
    int buttonPin;

    int state;

    public:
        KnobControl(int knobPinA, int knobPinB, int buttonPin);
        int readKnobValues();
        int readButtonValue();
};
