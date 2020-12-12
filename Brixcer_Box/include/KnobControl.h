class KnobControl {

    int knobPin;
    int buttonPin;

    public:
        KnobControl(int knobPin, int buttonPin);
        int readKnobValue();
        int readButtonValue();
};
