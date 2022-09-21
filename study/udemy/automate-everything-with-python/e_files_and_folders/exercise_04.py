from pprint import pprint
from pathlib import Path, PosixPath
from typing import Optional

from e_files_and_folders.constants import TEMP_FOLDER_PATH


def search_abs_path(search_exp: str, folder_path: PosixPath) -> list[Optional[str]]:
    return [path.absolute() for path in Path(folder_path).rglob(f"*{search_exp}*") if path.is_file()]


def main():
    pprint(search_abs_path("99", TEMP_FOLDER_PATH))


if __name__ == "__main__":
    main()
