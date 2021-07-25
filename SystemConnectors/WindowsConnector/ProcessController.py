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
            if session.Process and session.Process.name():
                name = session.Process.name()
                #  lastDot = name.rfind(".")
                process_names.append(name)  # [0:lastDot] if lastDot != -1 else name)
        return process_names
