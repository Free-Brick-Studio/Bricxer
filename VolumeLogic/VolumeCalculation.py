class VolumeCalculation:
    """Logic which controls how volume modifications are calculated."""

    max_volume = 0

    @staticmethod
    def convert_to_volume(start, value):
        """
        Calculates the new volume to set to based on current volume and new value.

        :param start: The current application volume.
        :param value: The value to modify the current volume by.
        :return: New volume level to set the application to.
        """
        return start + value
