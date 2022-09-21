from pathlib import Path, PosixPath

from e_files_and_folders.constants import PARENT_FOLDER_PATH


def iterate_sub_folders(folder_path: PosixPath) -> None:
    sub_folder_paths = Path(folder_path).iterdir()
    for sf in sub_folder_paths:
        print(f"{sf.name=}")
        print(f"{sf.is_dir()=}")
        print(f"{sf.is_file()=}\n")
        if sf.is_dir():
            iterate_sub_folders(sf)
        else:
            new_name = f"{folder_path.name}_{sf.stem}{sf.suffix}"
            new_path = Path.joinpath(folder_path, new_name)
            sf.rename(new_path)


def get_folder_tree(folder_path: PosixPath) -> None:
    folder_tree = Path(folder_path).glob("**/*")
    for leaf in folder_tree:
        print(f"{leaf.name=}")
        print(f"{leaf.is_dir()=}")
        print(f"{leaf.is_file()=}\n")
        if leaf.is_file():
            print(f"{leaf.parent.name=}\n")


def main():
    iterate_sub_folders(PARENT_FOLDER_PATH)

    get_folder_tree(PARENT_FOLDER_PATH)


if __name__ == "__main__":
    main()
