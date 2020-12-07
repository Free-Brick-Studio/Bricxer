"""
Interface for OS Connections to implement
"""
import abc
from VolumeLogic import Subject


class IOsConnection(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return \
            (hasattr(subclass, 'getSystemVolume') and callable(subclass.getSystemVolume)) and \
            (hasattr(subclass, 'getProcessVolume') and callable(subclass.getProcessVolume)) and \
            (hasattr(subclass, 'setSystemVolume') and callable(subclass.setSystemVolume)) and \
            (hasattr(subclass, 'setProcessVolume') and callable(subclass.setProcessVolume)) and \
            (hasattr(subclass, 'getRunningProcesses') and callable(subclass.getRunningProcesses)) and \
            (hasattr(subclass, 'play_pause') and callable(subclass.play_pause)) and \
            (hasattr(subclass, 'skip') and callable(subclass.skip)) and \
            (hasattr(subclass, 'reverse') and callable(subclass.reverse)) and \
            (hasattr(subclass, 'update') and callable(subclass.update))

    @abc.abstractmethod
    def getSystemVolume(self) -> int:
        """
        Get the system level volume
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getProcessVolume(self, processName: str) -> int:
        """
        Get the process level volume

        :param processName: The process to set the volume for.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def setSystemVolume(self, newVolume: int) -> None:
        """
        Set the system level volume

        :param newVolume: The volume to set it to.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def setProcessVolume(self, newVolume: int, processName: str) -> None:
        """
        Set the process volume

        :param newVolume: The volume to set it to.
        :param processName: The process to set the volume for.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getRunningProcesses(self) -> list:
        """
        Get the names of the processes currently running
        """
        raise NotImplementedError

    @abc.abstractmethod
    def play_pause(self) -> None:
        """
        Play or pause the media, based on system state.

        Playing state held by OS so we don't need to
        """
        raise NotImplementedError

    @abc.abstractmethod
    def skip(self) -> None:
        """
        Skip to the next media track
        """
        raise NotImplementedError

    @abc.abstractmethod
    def reverse(self) -> None:
        """
        Play the previous media track
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, subject: Subject, arg: object) -> None:
        """
        Updates the observer with new values from subject.

        :param subject: The object which notified of a change.
        :param arg: value that was changed.
        """
        raise NotImplementedError