from datetime import datetime
from pathlib import Path

from e_files_and_folders.constants import TEMP_FOLDER_PATH


EX_FOLDER_NAME = "exercise01"
EX_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, EX_FOLDER_NAME)


def main() -> None:
    for leaf in Path(EX_FOLDER_PATH).glob("**/*"):
        if leaf.is_file():
            leaf_st_ctime = leaf.stat().st_ctime
            date_created = datetime.fromtimestamp(leaf_st_ctime).strftime(
                "%Y-%m-%d_%H:%M:%S"
            )
            new_name = f"{leaf.stem}_{date_created}{leaf.suffix}"
            new_path = Path.joinpath(leaf.parent, new_name)
            leaf.rename(new_path)


if __name__ == "__main__":
    main()
