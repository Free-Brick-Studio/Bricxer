from SystemConnectors import IOsConnection
from WindowsConnector import VolumeMixer, ProcessController, MediaController
from VolumeLogic import ChangedValue


class WindowsConnector(IOsConnection):
    """
    OS Connection for Windows
    """

    def __init__(self):
        self.VolumeMixer = VolumeMixer()
        self.ProcessController = ProcessController()
        self.MediaController = MediaController()

    def get_system_volume(self):
        return self.VolumeMixer.get_system_volume()

    def get_process_volume(self, process_name):
        return self.VolumeMixer.get_process_volume(process_name)

    def set_system_volume(self, new_volume):
        return self.VolumeMixer.set_system_volume(new_volume)

    def set_process_volume(self, new_volume, process_name):
        return self.VolumeMixer.setProcessVolume(process_name, new_volume)

    def get_running_processes(self):
        return self.ProcessController.get_running_processes()

    def play_pause(self):
        return self.MediaController.play_pause()

    def skip(self):
        return self.MediaController.skip()

    def reverse(self):
        return self.MediaController.previous()
