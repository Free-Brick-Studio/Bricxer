import serial, serial.tools.list_ports
import time
from .ControllerReceiver import ControllerReceiver
from VolumeLogic import VolumeMixer, ChangedValue


class ControllerConnection:
    # TODO: Figure out how to set the BOARDNAME dynamically.
    BOARDNAME = "USB Serial Device (COM4)"

    #   The type of update,  The Mixer, App index   Associated value from the application
    _actions = {
        ChangedValue.VOLUME: lambda subject, index: int(subject.applications[index].volume),
        ChangedValue.COLOR: lambda subject, index: subject.applications[index].color_matrix,
    }

    def __init__(self, volume_mixer):
        self.volume_mixer = volume_mixer
        # TODO: Figure out how to set the port dynamically.
        self.serial = serial.Serial('COM4', 9600)
        ControllerReceiver(self).start()

    def send_to_controller(self, control, action, value):
        payload = str(control) + "." + str(action.value) + "." + str(value)
        self.serial.write(payload.encode())

    def receive_from_controller(self):
        controller_msg = self.serial.readline()
        data = controller_msg.decode("utf-8").strip().split(".")
        self.volume_mixer.modify_application(int(data[0]), ChangedValue(int(data[1])), int(data[2]))

    def connection_alive(self):
        com_ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        for com_port in com_ports:
            if self.BOARDNAME in com_port:
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
