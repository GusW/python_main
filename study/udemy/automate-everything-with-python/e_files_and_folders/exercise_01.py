from pathlib import Path


from e_files_and_folders.constants import TEMP_FOLDER_PATH

EX_FOLDER_NAME = "exercise01"
EX_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, EX_FOLDER_NAME)


def main():
    for leaf in Path(EX_FOLDER_PATH).glob("**/*"):
        if leaf.is_file():
            new_name = f"{leaf.parent.parent.name}-{leaf.parent.name}-{leaf.name}"
            new_path = Path.joinpath(leaf.parent, new_name)
            leaf.rename(new_path)


if __name__ == "__main__":
    main()
