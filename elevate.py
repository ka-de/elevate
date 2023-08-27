import sys
import ctypes

def run_as_admin():
    """
    Checks if the script is running with administrative privileges. 
    If not, it elevates the script's execution to run with admin rights on Windows.
    """
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        return  # Already running as admin, no need to elevate.

    # Run the main script as administrator
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    run_as_admin()