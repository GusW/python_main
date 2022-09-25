from l_image_processing.constants import EX_01_IMAGES_PATH, EX_01_GRAYIMAGES_PATH
from l_image_processing.to_grayscale import to_grayscale


def main() -> None:
    for file_path in EX_01_IMAGES_PATH.iterdir():
        to_grayscale(file_path, EX_01_GRAYIMAGES_PATH)


if __name__ == "__main__":
    main()
