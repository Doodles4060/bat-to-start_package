from sys import platform

from pathlib import Path

from warnings import warn
from typing import LiteralString, Union, Final, Any
from enum import Enum


class OSNamesEnum(str, Enum):
    AIX = 'aix'
    ANDROID = 'android'
    EMSCRIPTEN = 'emscripten'
    IOS = 'ios'
    LINUX = 'linux'
    MACOS = 'darwin'
    WINDOWS = 'win32'
    CYGWIN = 'cygwin'
    WASI = 'wasi'


class UnsupportedPlatform(Exception):
    pass


class MissingVenvFolder(Exception):
    pass


class BatToStart:
    _venv_activation_file: Final[str] = "activate"
    _invalid_path_warning_message: Final[str] = ("It seems like you're trying to create the .bat file in a different "
                                                 "folder than where your virtual environment is located. "
                                                 "Do you want to proceed? (Y/n)")

    @staticmethod
    def checkUserPlatform() -> None:
        os_name = platform
        if os_name != OSNamesEnum.WINDOWS.value:
            raise UnsupportedPlatform("Current version is the Windows only.")

    @staticmethod
    def proceedMenu() -> None:
        answer: str = input()
        while answer.lower() not in ["y", "n"]:
            print("Your response ('h') was not one of the expected responses: y, n,\nProceed (Y/n)")
            answer: str = input()
        if answer == "n":
            raise MissingVenvFolder()

    @classmethod
    def initialPathValidation(cls, root, initial_path) -> None:
        difference = root.relative_to(initial_path)
        if len(difference.parts) != 2:
            warn(cls._invalid_path_warning_message)
            cls.proceedMenu()

    @classmethod
    def findVenvActivationFile(cls, initial_path, venv_activation_file) -> Union[LiteralString, str, bytes]:
        for root, dirs, files in Path.walk(initial_path):
            if venv_activation_file in files:
                venv_activation_file_path = root / venv_activation_file

                cls.initialPathValidation(root, initial_path)
                return venv_activation_file_path

    @classmethod
    def createVenvStartBat(cls) -> None:
        cls.checkUserPlatform()

        initial_path: Path = Path().resolve()
        batch_file_path: Path = initial_path / "start.bat"

        venv_activation_path = cls.findVenvActivationFile(initial_path, cls._venv_activation_file)

        if venv_activation_path is None:
            raise FileNotFoundError("✗ No virtual environment activation file found ✗")

        # Batch file code. Maybe becomes configurable in near future.
        content = '@echo off\nchcp 65001 >nul\nstart cmd /k "{}"\n'.format(venv_activation_path)

        # Creating the batch file
        with open(batch_file_path, "w", encoding="utf-8") as batch_file:
            batch_file.write(content)

        print("✓ start.bat has been successfully created at {} ✓".format(batch_file_path))


if __name__ == '__main__':
    print(OSNamesEnum.__dict__)
