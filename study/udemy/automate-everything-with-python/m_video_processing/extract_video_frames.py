from pathlib import Path, PosixPath
from typing import Optional

from cv2 import VideoCapture, imwrite

from m_video_processing.constants import IMAGES_FOLDER_PATH, VIDEO_MP4_PATH


def extract_video_frames(
    video_path: PosixPath, output_path: PosixPath, target_frame: Optional[int] = 0
) -> None:
    video = VideoCapture(video_path.as_posix())
    count = 0
    while True:
        success, frame = video.read()
        if not success:
            break

        if target_frame:
            if target_frame > count:
                count += 1
                continue
            elif target_frame == count:
                imwrite(
                    Path.joinpath(output_path, f"{target_frame}.jpeg").as_posix(), frame
                )
            else:
                break
        else:
            count += 1
            imwrite(Path.joinpath(output_path, f"{count}.jpeg").as_posix(), frame)


def main():
    extract_video_frames(VIDEO_MP4_PATH, IMAGES_FOLDER_PATH)


if __name__ == "__main__":
    main()
