from pathlib import Path, PosixPath
from typing import Optional

from cv2 import VideoCapture, VideoWriter, VideoWriter_fourcc

from l_image_processing.detect_faces import detect_faces
from m_video_processing.constants import VIDEO_MP4_PATH, TEMP_FOLDER_PATH
from m_video_processing.extract_video_metadata import extract_video_metadata


def create_video_with_face_detector(
    video_path: PosixPath,
    output_path: PosixPath,
    file_name: Optional[str] = "",
    pattern: Optional[PosixPath] = None,
    is_blur: Optional[bool] = False,
    is_filled_rectangle: bool = False,
):
    video = VideoCapture(video_path.as_posix())
    video_metadata = extract_video_metadata(video_path)
    output = VideoWriter(
        Path.joinpath(
            output_path, file_name or "video_with_face_detection.avi"
        ).as_posix(),
        VideoWriter_fourcc(*"DIVX"),
        video_metadata.get("fps", 0),
        (video_metadata.get("width", 0), video_metadata.get("height", 0)),
    )
    count = 0
    while True:
        success, frame = video.read()
        if not success:
            break

        count += 1
        mod_frame = detect_faces(
            frame,
            video_path.name,
            pattern=pattern,
            is_blur=is_blur,
            is_filled_rectangle=is_filled_rectangle,
        )
        output.write(mod_frame)
        print(f"Processing {count}/{video_metadata.get('frame_count')}...")

    output.release()


def main():
    create_video_with_face_detector(VIDEO_MP4_PATH, TEMP_FOLDER_PATH)


if __name__ == "__main__":
    main()
