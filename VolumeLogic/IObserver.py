import abc
from . import Subject


class IObserver(metaclass=abc.ABCMeta):
    """Creates interface for classes that need to be notified of a change."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update') and
                callable(subclass.update))

    @abc.abstractmethod
    def update(self, subject: Subject, arg: object) -> None:
        """
        Updates the observer with new values from subject.

        :param subject: The object which notified of a change.
        :param arg: value that was changed.
        """
        raise NotImplementedError
