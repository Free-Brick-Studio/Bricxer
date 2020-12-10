from .. import IOsConnection
from . import VolumeMixer, ProcessController, MediaController


class WindowsConnection(IOsConnection):
    """
    OS Connection for Windows
    """

    def __init__(self):
        self.volume_mixer = VolumeMixer()
        self.process_controller = ProcessController()
        self.media_controller = MediaController()

    def get_system_volume(self):
        return self.volume_mixer.get_system_volume()

    def get_process_volume(self, process_name):
        return self.volume_mixer.get_process_volume(process_name)

    def set_system_volume(self, new_volume):
        return self.volume_mixer.set_system_volume(new_volume)

    def set_process_volume(self, new_volume, process_name):
        return self.volume_mixer.set_process_volume(process_name, new_volume)

    def get_running_processes(self):
        return self.process_controller.get_running_processes()

    def play_pause(self):
        return self.media_controller.play_pause()

    def skip(self):
        return self.media_controller.skip()

    def reverse(self):
        return self.media_controller.previous()
