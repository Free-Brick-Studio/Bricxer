from VolumeLogic import ChangedValue, IObserver, Subject


class VolumeMixer(IObserver, Subject):

    actions = {
        ChangedValue.VOLUME: lambda application, value: application.volume(value),
        ChangedValue.COLOR: lambda application, value: application.color_matrix(value),
    }

    def __init__(self):
        super().__init__()
        self.applications = [None] * 5
        self.modified_index = 0

    def update(self, subject: Subject, arg: object) -> None:
        for index, application in enumerate(self.applications):
            if application == subject:
                self.modified_index = index
                self.notify_all(arg)
                break

    def set_application(self, index, application):
        self.applications[index] = application
        self.modified_index = index
        self.notify_all(ChangedValue.APPLICATION)

    def modify_application(self, index, action, value):
        self.actions[action](self.applications[index], value)
