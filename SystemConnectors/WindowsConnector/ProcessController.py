"""
Process Controller for Windows
"""
from pycaw.pycaw import AudioUtilities


class ProcessController(): 

    def getRunningProcesses(self):
        """
        Get the currently running process names which can be controlled by pycaw
        """
        sessions = AudioUtilities.GetAllSessions()
        processNames = []
        for session in sessions:
            if session.Process and session.Process.name:
                processNames.append(session.Process.name())
        return processNames
