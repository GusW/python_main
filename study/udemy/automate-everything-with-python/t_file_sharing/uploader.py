from pathlib import Path, PosixPath
import requests

from t_file_sharing.constants import FILE_UPLOAD_POST_URI, TEMP_FOLDER_PATH


def upload(file_path: PosixPath, target_uri: str) -> None:
    file_ = open(file_path, mode="rb")
    req = requests.post(target_uri, files={"upfile": file_})
    print(req.text)


def main():
    upload(Path.joinpath(TEMP_FOLDER_PATH, "file.txt"), FILE_UPLOAD_POST_URI)


if __name__ == "__main__":
    main()
