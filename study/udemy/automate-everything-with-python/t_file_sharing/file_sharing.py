from functools import cache
from pathlib import Path

from filestack import Client

from t_file_sharing.constants import FILE_STACK_API_KEY, TEMP_FOLDER_PATH


@cache
def _generate_filestack_client():
    return Client(FILE_STACK_API_KEY)


def create_link_for(path: Path) -> str:
    client = _generate_filestack_client()
    link = client.upload(filepath=path.as_posix())
    return link.url


def main():
    path = Path.joinpath(TEMP_FOLDER_PATH, "myfile.txt")
    link = create_link_for(path)
    print(f"{link=}")


if __name__ == "__main__":
    main()
