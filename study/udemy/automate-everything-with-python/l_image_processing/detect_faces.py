from pathlib import Path, PosixPath
from typing import Optional

from cv2 import CascadeClassifier, imread, rectangle, imwrite, resize, addWeighted, blur

from l_image_processing.constants import TEMP_FOLDER_PATH


def get_face_cascade():
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


def _handle_face_detection(
    image,
    init_coordinates: tuple[int, int],
    end_coordinates: tuple[int, int],
    border_color: tuple[int, int, int] = (255, 255, 255),
    border_thickness: int = 3,
    pattern: Optional[PosixPath] = None,
    is_blur: bool = False,
    is_filled_rectangle: bool = False,
) -> None:
    face_x_init = init_coordinates[0]
    face_y_init = init_coordinates[1]
    face_x_end = end_coordinates[0]
    face_y_end = end_coordinates[1]

    if pattern:
        replacement = imread(pattern.as_posix(), 1)
        replacement_resized = resize(
            replacement, (face_x_end - face_x_init, face_y_end - face_y_init)
        )
        image[face_y_init:face_y_end, face_x_init:face_x_end] = addWeighted(
            image[face_y_init:face_y_end, face_x_init:face_x_end],
            0.1,
            replacement_resized,
            0.9,
            0,
        )
    else:
        if is_blur:
            image[face_y_init:face_y_end, face_x_init:face_x_end] = blur(
                image[face_y_init:face_y_end, face_x_init:face_x_end], (50, 50)
            )
        else:
            rectangle(
                image,
                init_coordinates,
                end_coordinates,
                border_color,
                -1 if is_filled_rectangle else border_thickness,
            )


def detect_faces(
    image,
    image_name: str,
    image_destination: Optional[PosixPath] = None,
    pattern: Optional[PosixPath] = None,
    is_blur: Optional[bool] = False,
    is_filled_rectangle: bool = False,
):
    detected_faces = get_face_cascade().detectMultiScale(image, 1.1, 4)
    if len(detected_faces) > 0:
        print(f"::: Faces detected in {image_name}")
        for x_pos, y_pos, width, height in detected_faces:
            _handle_face_detection(
                image,
                init_coordinates=(x_pos, y_pos),
                end_coordinates=(x_pos + width, y_pos + height),
                pattern=pattern,
                is_blur=is_blur,
                is_filled_rectangle=is_filled_rectangle,
            )

        if image_destination:
            imwrite(image_destination.as_posix(), image)
    else:
        print(f"!!! No faces detected in {image_name}")

    return image if not image_destination else None


def detect_faces_in_image(
    image_path: PosixPath, image_destination: Optional[PosixPath] = None
):
    image = imread(image_path.as_posix(), 1)
    image_name = image_path.name
    image_destination = _get_image_destination(image_path, image_destination)
    detect_faces(image, image_name, image_destination)


def main():
    image_path = Path.joinpath(TEMP_FOLDER_PATH, "humans.jpeg")
    detect_faces_in_image(image_path)


if __name__ == "__main__":
    main()
