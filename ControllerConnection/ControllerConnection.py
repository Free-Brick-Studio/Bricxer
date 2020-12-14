import serial
from ControllerConnection import ControllerReceiver
from VolumeLogic import VolumeMixer


class ControllerConnection():

    BOARDNAME = ""

    def __init__(self, volumeMixer):
        self.volumeMixer = volumeMixer
        self.serial = serial.Serial('address')
        ControllerReceiver(self)

    def send_to_controller(self, control, action, value):
        payload = control + "." + action + "." + value
        self.serial.open()
        self.serial.write(payload)
        self.serial.close()

    def receive_from_controller(self):
        controllerMsg = self.serial.readline()
        data = controllerMsg.split(".")
        self.volumeMixer.modify_application(data[0], data[1], data[2])

    def connectionAlive(self):
        comPorts = [tuple(p) for p in list(serial.tools.list_ports.comports)]
        for comPort in comPorts:
            if self.BOARDNAME in comPort:
                return True
        return False