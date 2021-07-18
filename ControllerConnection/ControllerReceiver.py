from threading import Thread


class ControllerReceiver(Thread):
    def __init__(self, controller_connection):
        Thread.__init__(self)
        self.connection = controller_connection
        self.daemon = True

    def run(self):
        while self.connection.connection_alive():
            self.connection.receive_from_controller()
