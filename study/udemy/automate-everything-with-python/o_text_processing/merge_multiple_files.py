from pathlib import Path, PosixPath
from typing import Optional

from o_text_processing.constants import TEMP_FOLDER_PATH
from o_text_processing.file_content_actions import (
    read_file_contents,
    create_file_with_contents,
)


def merge_files(
    file_paths: list[Optional[PosixPath]],
    merged_file_name: Optional[str] = "merged.txt",
    has_headers: bool = False,
) -> None:
    merged_contents = [
        "\n".join(
            read_file_contents(
                file_path
            ).splitlines()[  # could be achieved with file.readlines() instead of read()
                1 if idx > 0 and has_headers else 0 :
            ]
        )
        for idx, file_path in enumerate(file_paths)
    ]
    create_file_with_contents(
        Path.joinpath(TEMP_FOLDER_PATH, merged_file_name), "\n".join(merged_contents)
    )


def main():
    file_names = [f"file{num}.csv" for num in range(3, 7)]
    file_paths = [
        Path.joinpath(TEMP_FOLDER_PATH, file_name) for file_name in file_names
    ]
    merge_files(file_paths)
    merge_files(
        file_paths, merged_file_name="merged_without_headers.csv", has_headers=True
    )


if __name__ == "__main__":
    main()
