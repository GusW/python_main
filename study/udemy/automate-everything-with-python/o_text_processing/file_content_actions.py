from pathlib import Path, PosixPath
from typing import Optional

from o_text_processing.constants import TEMP_FOLDER_PATH


def create_file_with_contents(file_path: PosixPath, file_contents: str) -> None:
    with open(file_path, mode="w") as file_:
        file_.write(f"{file_contents}\n")


def read_file_contents(file_path: PosixPath) -> Optional[str]:
    with open(file_path, mode="r") as file_:
        return file_.read()


def main():
    # Create
    file_path = Path.joinpath(TEMP_FOLDER_PATH, "file_with_contents.txt")
    file_contents = """First text.



Last text."""
    create_file_with_contents(file_path, file_contents)

    # Read
    file1_contents = read_file_contents(file_path)
    print(f"{file1_contents=}")


if __name__ == "__main__":
    main()
