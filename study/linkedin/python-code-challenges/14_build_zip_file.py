import os
from zipfile import ZipFile
from pathlib import Path


_FOLDER_PATH = Path(__file__).parent.resolve()
_DATA_FOLDER = Path.joinpath(_FOLDER_PATH, "data", "my_stuff")


def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, "w") as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(
                        os.path.join(root, file), arcname=os.path.join(rel_path, file)
                    )


if __name__ == "__main__":
    zip_all(_DATA_FOLDER, [".jpg", ".txt"], "my_stuff.zip")
