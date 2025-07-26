import os
from pathlib import Path
from datetime import datetime
import traceback


def uni_cleaner():
    """
        Cleans up common temporary files from the user's Downloads folder.

        This function performs the following actions:
        - Identifies and deletes all `.rdp`, `.ica`, and `.crdownload` files in the Downloads directory.
        - Works cross-platform (Windows, macOS, Linux) by dynamically resolving the user's home directory.
        - Logs any errors that occur during the process to `/tmp/error_log.txt` with a timestamp and traceback.

        This is intended for use in automated cleanup scripts on systems where temporary
        remote session or browser files may accumulate in the Downloads folder.

        Returns:
            None
    """
    try:
        cwd = Path(os.path.join(os.path.expanduser("~"), "Downloads"))
        rdp_files = list((cwd).glob("*.rdp"))
        for file in rdp_files:
            file.unlink()
        ica_files = list((cwd).glob("*.ica"))
        for file in ica_files:
            file.unlink()
        cr_files = list((cwd).glob("*.crdownload"))
        for file in cr_files:
            file.unlink()


    except Exception as e:
        with open("/tmp/error_log.txt", "a") as error_log:
            error_log.write(f"Error occurred at {datetime.now()}:\n")
            error_log.write(traceback.format_exc() + "\n")



if __name__ == '__main__':
    uni_cleaner()
    exit()
