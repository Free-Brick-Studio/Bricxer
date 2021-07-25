from .. import IOsConnection
from . import AudioController, ProcessController, MediaController


class WindowsConnection(IOsConnection):
    """OS connection for Windows."""

    def __init__(self):
        self._audio_controller = AudioController()
        self._process_controller = ProcessController()
        self._media_controller = MediaController()

    def get_system_volume(self):
        return self._audio_controller.get_system_volume()

    def set_system_volume(self, new_volume):
        return self._audio_controller.set_system_volume(new_volume)

    def get_process_volume(self, process_name):
        return self._audio_controller.get_process_volume(process_name)

    def set_process_volume(self, new_volume, process_name):
        return self._audio_controller.set_process_volume(process_name, new_volume)

    def get_running_processes(self):
        return self._process_controller.get_running_processes()

    def play_pause(self):
        return self._media_controller.play_pause()

    def skip(self):
        return self._media_controller.skip()

    def reverse(self):
        return self._media_controller.previous()
