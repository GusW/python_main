from pathlib import Path, PosixPath

from e_files_and_folders.constants import TEMP_FOLDER_PATH


def safe_delete(file_path: PosixPath) -> None:
    """
    Replaces file content with empty byte
    """
    with open(file_path, "wb") as file_:
        file_.write(b"")
    file_path.unlink()


def main():
    files_to_delete = Path.joinpath(TEMP_FOLDER_PATH, "files_to_delete").glob("*.txt")
    for file_path in files_to_delete:
        safe_delete(file_path)


if __name__ == "__main__":
    main()
