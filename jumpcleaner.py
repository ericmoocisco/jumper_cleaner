import os
import platform
from pathlib import Path
from datetime import datetime
import traceback


def windows_cleaner():
    pass


def mac_cleaner():
    try:
        log_path = "/tmp/cron_test.txt"
        with open(log_path, "a") as f:
            f.write(f"Ran at {datetime.now()}\n")

            os.chdir('/Users/ericmoo/Downloads')
            f.write("Directory changed\n")

            cwd = Path.cwd()

            rdp_files = list(cwd.glob("*.rdp"))
            for file in rdp_files:
                file.unlink()
                f.write(f"Deleted RDP: {file}\n")

            ica_files = list(cwd.glob("*.ica"))
            for file in ica_files:
                file.unlink()
                f.write(f"Deleted ICA: {file}\n")


    except Exception as e:
        with open("/tmp/error_log.txt", "a") as error_log:
            error_log.write(f"Error occurred at {datetime.now()}:\n")
            error_log.write(traceback.format_exc() + "\n")


def test_cleaner():
    with open("/tmp/log.txt", "a") as f:
        try:
            os.chdir('/Users/ericmoo/Downloads')
            f.write("Directory changed\n")
            cwd = Path.cwd()
            log_path = "/tmp/cron_test.txt"
            all_files = list(cwd.glob("*"))
            f.write(f"Found {len(all_files)} total entries in Downloads:\n")
            for file in all_files:
                f.write(f"-> {file.name} (suffix: {file.suffix})\n")
        except Exception as e:
            f.write(f"{e}:\n")



if __name__ == '__main__':
    if platform.system() == 'Windows':
        pass
    if platform.system() == 'Darwin':
        mac_cleaner()
        exit()
    # else:
    #     test_cleaner()