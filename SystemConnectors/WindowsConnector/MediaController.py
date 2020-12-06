"""
Media controller for Windows
"""
import win32api
import enum


class KeyCodeEnum(enum.Enum):
    """
    Enums to represent the keycodes to send to manipluate playing media
    """
    SKIP = 0xB0
    PREV = 0xB1
    PLAY_PAUSE = 0xB3


class MediaController(object):
    """
    Keycodes to send to the operating system for corresponding action
    """
    
    def sendKeyPress(self, keycode):
        """
        Helper function to send the key press to Windows
        """
        hw = win32api.MapVirtualKey(keycode.value, 0)
        win32api.keybd_event(keycode.value, hw)

    def play_pause(self):
        """
        Send the Play / Pause keycode
        """
        self.sendKeyPress(KeyCodeEnum.PLAY_PAUSE)

    def skip(self):
        """
        Send the Skip keycode
        """
        self.sendKeyPress(KeyCodeEnum.SKIP)

    def previous(self):
        """
        Send the Previous keycode
        """
        self.sendKeyPress(KeyCodeEnum.PREV)
