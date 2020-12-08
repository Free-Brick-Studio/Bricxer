from VolumeLogic import ChangedValue, Subject, VolumeCalculation


class Application(Subject):
    """Application on the computer which can play sound."""

    os_connection = None

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.color_matrix = [0, 0, 0]

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def volume(self):
        return self.os_connection.getProcessVolume(self.name)

    @volume.setter
    def volume(self, value):
        volume = VolumeCalculation.convert_to_volume(self.volume, value)
        self.os_connection.setProcessVolume(volume, self.name)
        self.notify_all(ChangedValue.VOLUME)

    @property
    def color_matrix(self):
        return self.color_matrix

    @color_matrix.setter
    def color_matrix(self, color_matrix):
        self.color_matrix = color_matrix
        self.notify_all(ChangedValue.COLOR)
