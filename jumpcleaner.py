import os
import platform
from pathlib import Path
from datetime import datetime
import traceback


def uni_cleaner():
    try:
        cwd = Path(os.path.join(os.path.expanduser("~"), "Downloads"))
        rdp_files = list((cwd).glob("*.rdp"))
        for file in rdp_files:
            file.unlink()


        ica_files = list((cwd).glob("*.ica"))
        for file in ica_files:
            file.unlink()


    except Exception as e:
        with open("/tmp/error_log.txt", "a") as error_log:
            error_log.write(f"Error occurred at {datetime.now()}:\n")
            error_log.write(traceback.format_exc() + "\n")







if __name__ == '__main__':
    uni_cleaner()
    exit
