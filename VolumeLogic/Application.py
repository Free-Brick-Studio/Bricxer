from VolumeLogic import ChangedValue, Subject, VolumeCalculation


class Application(Subject):
    """Application on the computer which can play sound."""

    def __init__(self, name, volume):
        super().__init__()
        self.name = name
        self.volume = volume
        self.color_matrix = [0, 0, 0]

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def volume(self):
        return self.volume

    @volume.setter
    def volume(self, value):
        self.volume = VolumeCalculation.convert_to_volume(self.volume, value)
        self.notify_all(ChangedValue.VOLUME)

    @property
    def color_matrix(self):
        return self.color_matrix

    @color_matrix.setter
    def color_matrix(self, color_matrix):
        self.color_matrix = color_matrix
        self.notify_all(ChangedValue.COLOR)
