from pathlib import Path
from pprint import pprint

from e_files_and_folders.constants import FILES_FOLDER_PATH, TEMP_FOLDER_PATH


def handle_file_1(file_name: str) -> None:
    file_path = Path.joinpath(FILES_FOLDER_PATH, file_name)
    print(f"{type(file_path)=}\n")
    print(f"{file_path.name=}\n")
    print(f"{file_path.stem=}\n")
    print(f"{file_path.suffix=}\n")

    if file_path.exists():
        with open(file_path, "r") as open_file:
            print(f"{open_file.read()=}\n")


def handle_file_2(file_name: str) -> None:
    file_path = Path.joinpath(TEMP_FOLDER_PATH, file_name)
    if not file_path.exists():
        with open(file_path, "w") as f:
            f.write(f"This is a new file {file_name}.")


def iterate_folder(folder_name: str) -> Path.iterdir:
    folder_path = Path(folder_name)
    return folder_path.iterdir()


def main():
    handle_file_1("ghi.txt")

    handle_file_2("new.txt")

    files_folder = iterate_folder(FILES_FOLDER_PATH)
    print(f"{pprint(list(files_folder))}\n")

    temp_folder = iterate_folder(TEMP_FOLDER_PATH)
    print(f"{pprint(list(temp_folder))}\n")


if __name__ == "__main__":
    main()
