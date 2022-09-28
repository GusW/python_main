from pathlib import Path, PosixPath
from typing import Optional

from o_text_processing.constants import TEMP_FOLDER_PATH
from o_text_processing.file_content_actions import (
    read_file_contents,
    create_file_with_contents,
)


def _remove_trailing_comma(file_contents: Optional[str]) -> Optional[str]:
    content_list = file_contents.splitlines()
    modified_content = ""
    for content_row in content_list:
        if content_row[-1] == ",":
            modified_content += f"{content_row[:-1]}\n"
        else:
            modified_content += f"{content_row}\n"

    return modified_content


def handle_updates(
    file_path: PosixPath,
    target_string: Optional[str] = "",
    replacement: Optional[str] = "",
) -> None:
    file_contents = read_file_contents(file_path)
    if target_string:
        file_contents = file_contents.replace(target_string, replacement)

    modified_contents = _remove_trailing_comma(file_contents)
    create_file_with_contents(
        Path.joinpath(TEMP_FOLDER_PATH, f"modified_{file_path.stem}{file_path.suffix}"),
        modified_contents,
    )


def main():
    file_names = [f"file{num}.csv" for num in range(3, 7)]
    file_paths = [
        Path.joinpath(TEMP_FOLDER_PATH, file_name) for file_name in file_names
    ]

    for file_path in file_paths:
        handle_updates(file_path, target_string="amount", replacement="unit")


if __name__ == "__main__":
    main()
