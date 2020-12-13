class KnobControl {

    // Length of array for sending the value of knob readings
    static const int KNOBINPUTS = 2;

    int knobPinA;
    int knobPinB;
    int buttonPin;

    public:
        KnobControl(int knobPinA, int knobPinB, int buttonPin);
        int* readKnobValues();
        int readButtonValue();
};
