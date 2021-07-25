from .. import IOsConnection
from . import VolumeMixer, ProcessController, MediaController


class WindowsConnection(IOsConnection):
    """OS connection for Windows."""

    def __init__(self):
        self._volume_mixer = VolumeMixer()
        self._process_controller = ProcessController()
        self._media_controller = MediaController()

    def get_system_volume(self):
        return self._volume_mixer.get_system_volume()

    def set_system_volume(self, new_volume):
        return self._volume_mixer.set_system_volume(new_volume)

    def get_process_volume(self, process_name):
        return self._volume_mixer.get_process_volume(process_name)

    def set_process_volume(self, new_volume, process_name):
        return self._volume_mixer.set_process_volume(process_name, new_volume)

    def get_running_processes(self):
        return self._process_controller.get_running_processes()

    def play_pause(self):
        return self._media_controller.play_pause()

    def skip(self):
        return self._media_controller.skip()

    def reverse(self):
        return self._media_controller.previous()
