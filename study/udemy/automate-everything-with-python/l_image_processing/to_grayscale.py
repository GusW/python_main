from pathlib import Path, PosixPath

from cv2 import imread, imwrite

from l_image_processing.constants import TEMP_FOLDER_PATH


def load_colored_image(image_path: PosixPath):
    colored_pic = imread(
        image_path.as_posix(),
        1,  # 1 = colored, 0 = grayscale
    )
    print(f"{colored_pic=}\n")
    print(f"{colored_pic.ndim=}\n")
    print(f"{type(colored_pic)=}\n")
    return colored_pic


def to_grayscale(image_path: PosixPath, image_destination: PosixPath = None) -> str:
    grayscale_pic = imread(
        image_path.as_posix(),
        0,  # 1 = colored, 0 = grayscale´
    )

    image_destination = Path.joinpath(
        image_destination or image_path.parent,
        (
            image_path.name
            if image_destination
            else f"{image_path.stem}_grayscale{image_path.suffix}"
        ),
    )

    imwrite(
        image_destination.as_posix(),
        grayscale_pic,
    )


def main():
    image_path = Path.joinpath(TEMP_FOLDER_PATH, "galaxy.jpeg")
    to_grayscale(image_path)


if __name__ == "__main__":
    main()
