from pathlib import Path, PosixPath
from zipfile import ZipFile

from e_files_and_folders.constants import FILES_FOLDER_PATH, TEMP_FOLDER_PATH


def create_empty_files(file_names: list[str]) -> None:
    for name in file_names:
        file_path = Path.joinpath(TEMP_FOLDER_PATH, name)
        file_path.touch()


def create_archive_file(archive_name: str, file_paths: list[PosixPath]) -> None:
    archive_path = Path.joinpath(TEMP_FOLDER_PATH, archive_name)
    with ZipFile(archive_path, "w") as zf:
        for path in file_paths:
            zf.write(path)
            # delete files: path.unlink()


def unpack_archive_file(archive_path: PosixPath, destination_path: PosixPath) -> None:
    with ZipFile(archive_path, "r") as zf:
        zf.extractall(path=destination_path)


def main() -> None:
    file_names = [f"{idx}.txt" for idx in range(100, 112)]
    create_empty_files(file_names)

    file_paths = Path(TEMP_FOLDER_PATH).rglob("*.txt")
    create_archive_file("archive.zip", file_paths)

    for zf in Path(FILES_FOLDER_PATH).glob("*.zip"):
        unpack_archive_file(zf, Path.joinpath(TEMP_FOLDER_PATH, zf.stem))


if __name__ == "__main__":
    main()
