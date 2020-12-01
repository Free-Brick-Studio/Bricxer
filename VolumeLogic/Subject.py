class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify_all(self, arg):
        for observer in self.observers:
            observer.update(self, arg)
