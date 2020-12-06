import enum


class ChangedValue(enum.Enum):
    """Enum representing which value has been changed."""
    VOLUME = 0
    COLOR = 1
    APPLICATION = 2
