class KnobControl {

    // Length of array for sending the value of knob readings
    static const int KNOBINPUTS = 2;

    long buttonReadTime = 0;

    int count = 0;

    int knobPinA;
    int knobPinB;
    int buttonPin;

    public:
        KnobControl(int knobPinA, int knobPinB, int buttonPin);
        int readKnobValues();
        int readButtonValue();
};
