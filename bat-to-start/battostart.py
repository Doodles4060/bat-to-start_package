from pathlib import Path

from os import walk
from os.path import join

from typing import LiteralString, Union


def find_venv_activation_file(initial_dir, venv_activation_file) -> Union[LiteralString, str, bytes]:
    for root, dirs, files in walk(initial_dir):
        if venv_activation_file in files:
            return join(root, venv_activation_file)


def create_venv_start_bat() -> None:
    initial_dir = Path().resolve()

    venv_activation_file = "activate"
    venv_activation_path = find_venv_activation_file(initial_dir, venv_activation_file)

    if venv_activation_path is None:
        raise FileNotFoundError("No virtual environment found")

    batch_file_path = initial_dir / "start.bat"

    # Content for the batch file
    content = '@echo off\nchcp 65001 >nul\nstart cmd /k "{}"\n'.format(venv_activation_path)

    # Write the batch file
    with open(batch_file_path, "w", encoding="utf-8") as batch_file:
        batch_file.write(content)

    print("✓ start.bat has been successfully created at {} ✓".format(batch_file_path))


if __name__ == "__main__":
    create_venv_start_bat()
