import os
import platform


def windows_cleaner():
    pass


def mac_cleaner():
    from pathlib import Path
    os.chdir('/Users/ericmoo/Downloads')
    cwd = Path.cwd()
    for file in cwd.rglob("*.rdp"):
        file.unlink()
    for file in cwd.rglob("*.ica"):
        file.unlink()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        pass
    if platform.system() == 'Darwin':
        mac_cleaner()
        exit()