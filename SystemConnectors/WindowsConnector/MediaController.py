"""
Media controller for Windows
"""
import win32api

class MediaController(object):
    """
    Keycodes to send to the operating system for corresponding action
    """
    PLAY_PAUSE_KEYCODE = 0xB3
    SKIP_KEYCODE = 0xB0
    PREV_KEYCODE = 0xB1

    """
    Helper function to send the key press to Windows
    """
    def sendKeyPress(self, keycode):
        hw = win32api.MapVirtualKey(keycode, 0)
        win32api.keybd_event(keycode, hw)

    """
    Send the Play / Pause keycode
    """
    def play_pause(self):
        self.sendKeyPress(self.PLAY_PAUSE_KEYCODE)

    """
    Send the Skip keycode
    """
    def skip(self):
        self.sendKeyPress(self.SKIP_KEYCODE)

    """
    Send the Previous keycode
    """
    def previous(self):
        self.sendKeyPress(self.PREV_KEYCODE)

if __name__ == "__main__":
    MC = MediaController()
    MC.play_pause()