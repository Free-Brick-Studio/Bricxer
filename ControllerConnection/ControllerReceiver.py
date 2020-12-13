from ControllerConnection import ControllerConnection


class ControllerReceiver():
    def __init__(self, controllerConnection):
        self.connection = controllerConnection

    def loop(self):
        while self.connection.connectionAlive():
            self.connection.receive_from_controller()


if __name__ == "__main__":
    pass