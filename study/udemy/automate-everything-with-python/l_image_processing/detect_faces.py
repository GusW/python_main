from pathlib import Path, PosixPath
from typing import Optional

from cv2 import CascadeClassifier, imread, rectangle, imwrite

from l_image_processing.constants import TEMP_FOLDER_PATH


def _get_face_cascade():
    face_xml_path = Path.joinpath(TEMP_FOLDER_PATH, "faces.xml")
    return CascadeClassifier(face_xml_path.as_posix())


def _get_image_destination(
    image_path: PosixPath, image_destination: Optional[PosixPath] = None
):
    return Path.joinpath(
        image_destination or image_path.parent,
        (
            image_path.name
            if image_destination
            else f"{image_path.stem}_detected_faces{image_path.suffix}"
        ),
    )


def detect_faces(image_path: PosixPath, image_destination: Optional[PosixPath] = None):
    image = imread(image_path.as_posix(), 1)
    image_name = image.name
    detected_faces = _get_face_cascade().detectMultiScale(image, 1.1, 4)
    if len(detected_faces) > 0:
        print(f"::: Faces detected in {image_name}")
        for x_pos, y_pos, width, height in detected_faces:
            rectangle(
                image, (x_pos, y_pos), (x_pos + width, y_pos + height), (255, 0, 0), 3
            )

        image_destination = _get_image_destination(image_path, image_destination)
        imwrite(image_destination.as_posix(), image)
    else:
        print(f"!!! No faces detected in {image_name}")


def main():
    image_path = Path.joinpath(TEMP_FOLDER_PATH, "humans.jpeg")
    detect_faces(image_path)


if __name__ == "__main__":
    main()
