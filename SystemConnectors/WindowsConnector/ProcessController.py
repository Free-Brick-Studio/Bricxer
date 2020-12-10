"""
Process Controller for Windows
"""
from pycaw.pycaw import AudioUtilities


class ProcessController:

    def get_running_processes(self):
        """
        Get the currently running process names which can be controlled by pycaw
        """
        sessions = AudioUtilities.GetAllSessions()
        process_names = []
        for session in sessions:
            if session.Process and session.Process.name:
                process_names.append(session.Process.name())
        return process_names
