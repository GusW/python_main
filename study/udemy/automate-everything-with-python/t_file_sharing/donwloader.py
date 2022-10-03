from pathlib import Path, PosixPath
import requests

from t_file_sharing.constants import MP3_URI_PREFIX, TEMP_FOLDER_PATH


def download(uri: str, local_file_path: PosixPath) -> None:
    req = requests.get(uri)
    with open(local_file_path, mode="wb") as file_:
        file_.write(req.content)


def main():
    file_uri = f"{MP3_URI_PREFIX}Symphony%20No.6%20(1st%20movement).mp3"
    local_file_path = Path.joinpath(TEMP_FOLDER_PATH, "download.mp3")
    download(file_uri, local_file_path)


if __name__ == "__main__":
    main()
