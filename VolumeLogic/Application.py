from . import ChangedValue, VolumeCalculation
from .Subject import Subject


class Application(Subject):
    """Application on the computer which can play sound."""

    os_connection = None

    def __init__(self, name):
        super().__init__()
        self._name = name
        self._color_matrix = [0, 0, 0]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def volume(self):
        return self.os_connection.get_process_volume(self.name)

    @volume.setter
    def volume(self, value):
        volume = VolumeCalculation.convert_to_volume(self.volume, value)
        self.os_connection.set_process_volume(volume, self.name)
        self.notify_all(ChangedValue.VOLUME)

    @property
    def color_matrix(self):
        return self._color_matrix

    @color_matrix.setter
    def color_matrix(self, color_matrix):
        self._color_matrix = color_matrix
        self.notify_all(ChangedValue.COLOR)
