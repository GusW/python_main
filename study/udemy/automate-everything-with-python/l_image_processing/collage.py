from pathlib import Path, PosixPath

from cv2 import imread, imwrite
import numpy as np

from l_image_processing.constants import COLLAGE_FOLDER_PATH


def create_collage(
    images_folder: PosixPath,
    rows: int = 0,
    cols: int = 0,
    margin_horizontal: int = 0,
    margin_vertical: int = 0,
    image_destination: PosixPath = None,
) -> None:
    if image_paths := list(images_folder.iterdir()):
        # if all pictures have the same shape:
        image_height, image_width, image_bands = imread(image_paths[0].as_posix()).shape

        collage = np.zeros(
            (
                image_height * rows + margin_horizontal * (rows + 1),
                image_width * cols + margin_vertical * (cols + 1),
                image_bands,
            ),
            np.uint8,
        )
        collage.fill(255)  # fill with white instead of default black

        positions = [(r, c) for r in range(rows) for c in range(cols)]
        for (pos_y, pos_x), image_path in zip(positions, image_paths):
            y = pos_y * (image_height + margin_horizontal) + margin_horizontal
            y_range = y + image_height
            x = pos_x * (image_width + margin_vertical) + margin_vertical
            x_range = x + image_width
            collage[y:y_range, x:x_range] = imread(image_path.as_posix())

        imwrite(image_destination.as_posix(), collage)


def main():
    cols = 3
    rows = 2
    margin_horizontal = 20
    margin_vertical = 20
    create_collage(
        COLLAGE_FOLDER_PATH,
        rows=rows,
        cols=cols,
        margin_horizontal=margin_horizontal,
        margin_vertical=margin_vertical,
        image_destination=Path.joinpath(COLLAGE_FOLDER_PATH, "collage.jpeg"),
    )


if __name__ == "__main__":
    main()
