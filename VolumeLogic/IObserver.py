import abc
from VolumeLogic import Subject


class IObserver(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update') and
                callable(subclass.update) or
                NotImplemented)

    @abc.abstractmethod
    def update(self, subject: Subject, arg: object) -> None:
        """Update the observer with new values from subject"""
        raise NotImplementedError
