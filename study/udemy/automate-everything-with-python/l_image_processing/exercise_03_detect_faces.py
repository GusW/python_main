from pathlib import Path

from l_image_processing.constants import EX_03_IMAGES_PATH, EX_03_WITH_FACES_PATH
from l_image_processing.detect_faces import detect_faces


def main():
    for file_path in Path(EX_03_IMAGES_PATH).iterdir():
        detect_faces(file_path, EX_03_WITH_FACES_PATH)


if __name__ == "__main__":
    main()
