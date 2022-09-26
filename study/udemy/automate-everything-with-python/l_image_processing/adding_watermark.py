from pathlib import Path, PosixPath
from typing import Optional

import cv2

from l_image_processing.constants import TEMP_FOLDER_PATH


def _get_image_destination(
    image_path: PosixPath, image_destination: Optional[PosixPath] = None
) -> str:
    return Path.joinpath(
        image_destination or image_path.parent,
        (
            image_path.name
            if image_destination
            else f"{image_path.stem}_with_watermark{image_path.suffix}"
        ),
    ).as_posix()


def add_watermark(
    image_path: PosixPath,
    watermark_path: PosixPath,
    image_destination: Optional[PosixPath] = None,
) -> None:
    image_destination = _get_image_destination(image_path, image_destination)
    image = cv2.imread(image_path.as_posix(), 1)
    watermark = cv2.imread(watermark_path.as_posix(), 1)

    image_height, image_width, *_ = image.shape
    watermark_height, watermark_width, *_ = watermark.shape

    watermark_x_pos = image_width - watermark_width
    watermark_y_pos = image_height - watermark_height

    image[watermark_y_pos:, watermark_x_pos:] = cv2.addWeighted(
        image[watermark_y_pos:, watermark_x_pos:], 0.5, watermark, 0.5, 0
    )
    cv2.imwrite(image_destination, image)


def main():
    image_path = Path.joinpath(TEMP_FOLDER_PATH, "elves.jpeg")
    watermark_path = Path.joinpath(TEMP_FOLDER_PATH, "watermark.png")
    add_watermark(image_path, watermark_path)


if __name__ == "__main__":
    main()
