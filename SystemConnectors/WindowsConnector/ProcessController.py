from pycaw.pycaw import AudioUtilities


class ProcessController:
    """Process controller for Windows."""

    @staticmethod
    def get_running_processes():
        """
        Get the currently running process names which can be controlled.
        """
        process_names = []

        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name():
                name = session.Process.name()
                process_names.append(name)

        return process_names
