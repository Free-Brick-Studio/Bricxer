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

    def getSystemVolume(self):
        return self.VolumeMixer.getSystemVolume()

    def getProcessVolume(self, processName):
        return self.VolumeMixer.getProcessVolume(processName)

    def setSystemVolume(self, newVolume):
        return self.VolumeMixer.setSystemVolume(newVolume)

    def setProcessVolume(self, newVolume, processName):
        return self.VolumeMixer.setProcessVolume(processName, newVolume)

    def getRunningProcesses(self):
        return self.ProcessController.getRunningProcesses()

    def play_pause(self):
        return self.MediaController.play_pause()

    def skip(self):
        return self.MediaController.skip()

    def reverse(self):
        return self.MediaController.previous()

    def update(self, subject, arg):
        if (arg != ChangedValue.VOLUME):
            return

        application = subject.applications[subject.modified_index]
        if application.name == "System":
            self.setSystemVolume(application.volume)
        else:
            self.setProcessVolume(application.volume, application.name)
