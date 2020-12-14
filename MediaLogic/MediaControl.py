class MediaControl:

    def __init__(self, os_connection):
        self._os_connection = os_connection

    def play_pause(self):
        """
        Tells the OS to play/pause the current running media.
        """
        self._os_connection.play_pause()

    def reverse(self):
        """
        Tells the OS to go back to the start or previous media.
        """
        self._os_connection.reverse()

    def skip(self):
        """
        Tells the OS to skip to the end or next media.
        """
        self._os_connection.skip()
