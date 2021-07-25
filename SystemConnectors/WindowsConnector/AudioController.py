from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class AudioController:
    """Audio controller for Windows."""

    def get_system_volume(self):
        """
        Get the current volume of the system
        """
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume.GetMasterVolumeLevel()

    def set_system_volume(self, volume):
        """
        Set the system volume

        volume : Int - The value to set the system volume to
        """
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(volume, None)

    @staticmethod
    def get_process_volume(process_name):
        """
        Get the current volume of the process.

        :param process_name: The name of the process to get the volume for.
        """
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == process_name:
                mixer = session.SimpleAudioVolume
                return mixer.GetMasterVolume() * 100

        return 0

    @staticmethod
    def set_process_volume(process_name, volume):
        """
        Set the current volume of the process.

        :param process_name: The name of the process to get the volume for.
        :param volume: The value to set the system volume to.
        """
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == process_name:
                mixer = session.SimpleAudioVolume
                temp = min(1, max(0, volume / 100))
                mixer.SetMasterVolume(temp, None)
