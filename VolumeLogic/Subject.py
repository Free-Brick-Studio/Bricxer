class Subject:
    """Object which notifies observers when modified."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Attaches an observer to the subject.

        :param observer: Object which should be notified when this object changes.
        """
        self._observers.append(observer)

    def notify_all(self, arg):
        """
        Notifies all attached observers that a change has occurred.

        :param arg: Object to tell observers which value has been modified.
        """
        for observer in self._observers:
            observer.update(self, arg)
