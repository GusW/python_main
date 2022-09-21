from pathlib import Path, PosixPath

from e_files_and_folders.constants import TEMP_FOLDER_PATH


def rename_folder_files(
    folder_path: PosixPath, prefix: str = "", suffix: str = ""
) -> None:
    file_paths = Path(folder_path).iterdir()
    for path in file_paths:
        new_name = f"{prefix}{path.stem}{suffix}{path.suffix}"
        new_path = Path.joinpath(folder_path, new_name)
        # OR: new_path = path.with_name(new_name)
        if not new_path.exists():
            path.rename(new_path)


def main():
    rename_folder_files(TEMP_FOLDER_PATH, prefix="renamed_", suffix="_again")


if __name__ == "__main__":
    main()
