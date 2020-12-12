class LedControl {

    static const int COLORS = 3;

    int ledPin;
    int volume;
    int color_matrix[COLORS];

    public:
        LedControl(int ledPin);
        void setVolume(int volume);
        void setColorMatrix(int* matrix);
};
