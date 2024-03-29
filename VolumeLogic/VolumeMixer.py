from .Application import Application
from .ChangedValue import ChangedValue
from .IObserver import IObserver
from .Subject import Subject


class VolumeMixer(IObserver, Subject):
    """Collection of Applications whose volume is being controlled."""

    _num_of_knobs = 5
    _actions = {
        ChangedValue.VOLUME: lambda application, value: setattr(application, "volume", value),
        ChangedValue.COLOR: lambda application, value: setattr(application, "color_matrix", value),
    }

    def __init__(self, os_connection):
        super().__init__()
        self._os_connection = os_connection
        Application.os_connection = os_connection
        self._applications = [None] * self._num_of_knobs

    def update(self, subject, arg):
        for index, application in enumerate(self._applications):
            if application == subject:
                self.notify_all((index, arg))
                break

    @property
    def applications(self) -> list:
        return self._applications

    @applications.setter
    def applications(self, applications):
        self._applications = applications

    def get_running_applications(self):
        """
        Gets the names of all the applications currently running on the computer.

        :return: List of names of the applications from the computer.
        """
        return self._os_connection.get_running_processes()

    def set_application(self, index: int, name):
        """
        Sets the application whose volume will be controlled by the knob in the indexed position.

        :param index: Relation to which knob will control the volume of the application.
        :param name: Name of the application whose volume is being controlled.
        """
        self.applications[index] = Application(name)
        self.applications[index].attach(self)
        self.notify_all((index, ChangedValue.APPLICATION))

    def modify_application(self, index, action, value):
        """
        Modified the application at the indexed position.

        Modified values can include volume or color.

        :param index: Relation to which knob will control the volume of the application.
        :param action: Which property of the application is being modified.
        :param value: The value to set the application property to.
        """
        self._actions[action](self.applications[index], value)
