from pathlib import Path

from e_files_and_folders.constants import TEMP_FOLDER_PATH


EX_FOLDER_NAME = "exercise03"
EX_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, EX_FOLDER_NAME)


def main() -> None:
    for leaf in Path(EX_FOLDER_PATH).rglob("*.txt"):
        if leaf.is_file():
            new_path = leaf.with_suffix(".csv")
            leaf.rename(new_path)


if __name__ == "__main__":
    main()
