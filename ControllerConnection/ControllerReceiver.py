from threading import Thread

class ControllerReceiver(Thread):
    def __init__(self, controllerConnection):
        Thread.__init__(self)
        self.connection = controllerConnection

    def run(self):
        while self.connection.connectionAlive():
            self.connection.receive_from_controller()
