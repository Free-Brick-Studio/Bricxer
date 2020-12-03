"""
Volume Mixer for Windows
"""
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeMixer(object):
    """
    Get the current volume of the system
    """
    def getSystemVolume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume.GetMasterVolumeLevel()

    """
    Get the current volume of the process

    processName : String - The name of the process to get the volume for
    """
    def getProcessVolume(processName):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == processName:
                mixer = session.SimpleAudioVolume
                return mixer.GetMasterVolume
        return 0
    
    """
    Set the system volume

    volume : Int - The value to set the system volume to
    """
    def setSystemVolume(volume):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(volume, None)
        return False

    """
    Get the current volume of the process

    processName : String - The name of the process to get the volume for
    volume      : Int    - The value to set the system volume to
    """
    def setProcessVolume(processName, volume):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == processName:
                mixer = session.SimpleAudioVolume
                mixer.SetMasterVolume(volume)
                return True
        return False
