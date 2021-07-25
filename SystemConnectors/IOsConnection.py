"""
Interface for OS Connections to implement
"""
import abc


class IOsConnection(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return \
            (hasattr(subclass, 'get_system_volume') and callable(subclass.get_system_volume)) and \
            (hasattr(subclass, 'get_process_volume') and callable(subclass.get_process_volume)) and \
            (hasattr(subclass, 'set_system_volume') and callable(subclass.set_system_volume)) and \
            (hasattr(subclass, 'set_process_volume') and callable(subclass.set_process_volume)) and \
            (hasattr(subclass, 'get_running_processes') and callable(subclass.get_running_processes)) and \
            (hasattr(subclass, 'play_pause') and callable(subclass.play_pause)) and \
            (hasattr(subclass, 'skip') and callable(subclass.skip)) and \
            (hasattr(subclass, 'reverse') and callable(subclass.reverse))

    @abc.abstractmethod
    def get_system_volume(self) -> int:
        """
        Get the system level volume.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_process_volume(self, process_name: str) -> int:
        """
        Get the process level volume.

        :param process_name: The process to set the volume for.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_system_volume(self, new_volume: int) -> None:
        """
        Set the system level volume.

        :param new_volume: The volume to set it to.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_process_volume(self, new_volume: int, process_name: str) -> None:
        """
        Set the process volume.

        :param new_volume: The volume to set it to.
        :param process_name: The process to set the volume for.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_running_processes(self) -> list:
        """
        Get the names of the processes currently running.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def play_pause(self) -> None:
        """
        Play or pause the media, based on system state.

        Playing state held by OS so we don't need to.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def skip(self) -> None:
        """
        Skip to the next media track.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def reverse(self) -> None:
        """
        Play the previous media track.
        """
        raise NotImplementedError
