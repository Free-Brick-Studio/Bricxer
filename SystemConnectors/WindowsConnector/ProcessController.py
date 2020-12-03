"""
Process Controller for Windows
"""
from pycaw.pycaw import AudioUtilities

class ProcessController(): 
    """
    Get the currently running process names which can be controlled by pycaw
    """
    def getRunningProcesses(self):
        sessions = AudioUtilities.GetAllSessions()
        processNames = []
        for session in sessions:
            if session.Process and session.Process.name:
                processNames.append(session.Process.name())
        return processNames
        
if __name__ == "__main__":
    PC = ProcessController()
    print (PC.getRunningProcesses())