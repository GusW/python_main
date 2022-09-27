from pathlib import Path, PosixPath
from typing import Optional

from cv2 import imread, resize, imwrite
import numpy as np

from l_image_processing.constants import TEMP_FOLDER_PATH


def _get_image_destination(
    image_path: PosixPath, image_destination: Optional[PosixPath] = None
) -> str:
    return Path.joinpath(
        image_destination or image_path.parent,
        (
            image_path.name
            if image_destination
            else f"{image_path.stem}_changed_background{image_path.suffix}"
        ),
    ).as_posix()


def change_background(
    foreground_path: PosixPath,
    background_path: PosixPath,
    image_destination: Optional[PosixPath] = None,
) -> None:
    image_destination = _get_image_destination(foreground_path, image_destination)
    foreground = imread(foreground_path.as_posix(), 1)
    background = imread(background_path.as_posix(), 1)

    foreground_height, foreground_width, *_ = foreground.shape
    background_resized = resize(background, (foreground_width, foreground_height))

    for i in range(foreground_height):
        for j in range(foreground_width):
            if np.any(foreground[i, j] == [1, 255, 10]):
                foreground[i, j] = background_resized[i, j]

    imwrite(image_destination, foreground)


def main():
    foreground_path = Path.joinpath(TEMP_FOLDER_PATH, "giraffe.jpeg")
    background_path = Path.joinpath(TEMP_FOLDER_PATH, "safari.jpeg")
    change_background(foreground_path, background_path)


if __name__ == "__main__":
    main()
