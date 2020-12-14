import serial, serial.tools.list_ports
import time
from .ControllerReceiver import ControllerReceiver
from VolumeLogic import VolumeMixer, ChangedValue


class ControllerConnection():
    # TODO: Figure out how to set the BOARDNAME dynamically.
    BOARDNAME = "USB Serial Device (COM4)"

    #   The type of update,  The Mixer, App index   Associated value from the application
    _actions = {
        ChangedValue.VOLUME: lambda subject, index: subject.applications[index].volume,
        ChangedValue.COLOR: lambda subject, index: subject.applications[index].color_matrix,
    }

    def __init__(self, volumeMixer):
        self.volumeMixer = volumeMixer
        # TODO: Figure out how to set the port dynamically.
        self.serial = serial.Serial('COM4', 9600)
        ControllerReceiver(self).start()

    def send_to_controller(self, control, action, value):
        payload = str(control) + "." + str(action) + "." + str(value)
        self.serial.write(payload.encode())

    def receive_from_controller(self):
        controllerMsg = self.serial.readline()
        data = controllerMsg.decode("utf-8").split(".")
        self.volumeMixer.modify_application(data[0], data[1], data[2])

    def connectionAlive(self):
        comPorts = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        for comPort in comPorts:
            if self.BOARDNAME in comPort:
                return True
        return False

    def update(self, subject, arg):
        # TODO: Send both volume and color
        if arg[1] == ChangedValue.APPLICATION:
            self._actions[ChangedValue.VOLUME](subject, arg[0])
            self._actions[ChangedValue.COLOR](subject, arg[0])
            return
        updated = self._actions[arg[1]](subject, arg[0])
        self.send_to_controller(arg[0], arg[1], updated)
