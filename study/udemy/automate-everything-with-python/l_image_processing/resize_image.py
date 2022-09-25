from pathlib import Path, PosixPath

import cv2

from l_image_processing.constants import TEMP_FOLDER_PATH


def calculate_size(
    scale_percentage: float, width: float, height: float
) -> tuple[int, int]:
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)


def resize_image(
    image_path: PosixPath,
    scale_percentage: float = 1.0,
    image_destination: PosixPath = None,
) -> str:

    image_destination = Path.joinpath(
        image_destination or image_path.parent,
        (
            image_path.name
            if image_destination
            else f"{image_path.stem}_resized{image_path.suffix}"
        ),
    )

    image = cv2.imread(image_path.as_posix())
    height, width, *_ = image.shape
    resized_image = cv2.resize(
        image, dsize=calculate_size(scale_percentage, width, height)
    )

    cv2.imwrite(
        image_destination.as_posix(),
        resized_image,
    )


def main():
    image_path = Path.joinpath(TEMP_FOLDER_PATH, "galaxy.jpeg")
    resize_image(image_path, 20)


if __name__ == "__main__":
    main()
