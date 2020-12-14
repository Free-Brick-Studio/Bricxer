from VolumeLogic import VolumeMixer
from SystemConnectors import WindowsConnection
from UI import FrontEnd

if __name__ == '__main__':
    """
    Starts up the backend and launches the front end
    """
    os_connection = WindowsConnection()
    volume_mixer = VolumeMixer(os_connection)
    FrontEnd(volume_mixer).launch()
