from VolumeLogic import Application, ChangedValue, IObserver, Subject
from SystemConnectors import IOsConnection


class VolumeMixer(IObserver, Subject):
    """Collection of Applications whose volume is being controlled."""

    num_of_knobs = 5
    actions = {
        ChangedValue.VOLUME: lambda application, value: application.volume(value),
        ChangedValue.COLOR: lambda application, value: application.color_matrix(value),
    }

    def __init__(self, os_connection: IOsConnection):
        super().__init__()
        self.os_connection = os_connection
        Application.os_connection = os_connection
        self.applications = [None] * self.num_of_knobs
        self.modified_index = 0

    def update(self, subject, arg):
        for index, application in enumerate(self.applications):
            if application == subject:
                self.modified_index = index
                self.notify_all(arg)
                break

    def set_application(self, index, application):
        """
        Sets the application whose volume will be controlled by the knob in the indexed position.

        :param index: Relation to which knob will control the volume of the application.
        :param application: Application whose volume is being controlled.
        """
        self.applications[index] = application
        self.modified_index = index
        self.notify_all(ChangedValue.APPLICATION)

    def modify_application(self, index, action, value):
        """
        Modified the application at the indexed position.

        Modified values can include volume or color.

        :param index: Relation to which knob will control the volume of the application.
        :param action: Which property of the application is being modified.
        :param value: The value to set the application property to.
        """
        self.actions[action](self.applications[index], value)
