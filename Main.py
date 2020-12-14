from VolumeLogic import ChangedValue, VolumeMixer
from SystemConnectors import WindowsConnection
from UI import FrontEnd
from sys import argv

if __name__ == '__main__':
    """
    Starts up the backend and launches the front end
    """
    os_connection = WindowsConnection()
    volume_mixer = VolumeMixer(os_connection)
    FrontEnd(volume_mixer).launch()
