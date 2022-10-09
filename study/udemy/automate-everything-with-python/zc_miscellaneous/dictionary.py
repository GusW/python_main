from pathlib import Path
from typing import Optional
import json

from zc_miscellaneous.constants import TEMP_FOLDER_PATH


def define(word: str) -> list[Optional[str]]:
    with open(Path.joinpath(TEMP_FOLDER_PATH, "data.json")) as file_:
        data = json.load(file_)
        return data.get(word.lower(), ["Definition not found."])


def main():
    word = input("Enter a word: ")
    for idx, definition in enumerate(define(word), 1):
        print(f"{idx}: {definition}\n")


if __name__ == "__main__":
    main()
