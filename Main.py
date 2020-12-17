from VolumeLogic import VolumeMixer
from SystemConnectors import WindowsConnection
from UI import FrontEnd
from ControllerConnection import ControllerConnection

if __name__ == '__main__':
    """
    Starts up the backend and launches the front end
    """
    os_connection = WindowsConnection()
    volume_mixer = VolumeMixer(os_connection)
    controller_connection = ControllerConnection(volume_mixer)
    volume_mixer.attach(controller_connection)
    FrontEnd(volume_mixer).launch()
