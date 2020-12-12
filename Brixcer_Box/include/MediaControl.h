class MediaControl {

    static const int BUTTONS = 3;

    int togglePlayPausePin;
    int previousPin;
    int nextPin;

    public:
        MediaControl(int playPausePin, int previousPin, int nextPin);
        int* readButtonValues();
};
