from pathlib import PosixPath

from cv2 import (
    CAP_PROP_FPS,
    CAP_PROP_FRAME_COUNT,
    CAP_PROP_FRAME_HEIGHT,
    CAP_PROP_FRAME_WIDTH,
    VideoCapture,
)

from m_video_processing.constants import VIDEO_MP4_PATH


def extract_video_metadata(video_path: PosixPath):
    video = VideoCapture(video_path.as_posix())
    return {
        "width": int(video.get(CAP_PROP_FRAME_WIDTH)),
        "height": int(video.get(CAP_PROP_FRAME_HEIGHT)),
        "frame_count": video.get(CAP_PROP_FRAME_COUNT),
        "fps": video.get(CAP_PROP_FPS),
    }


def main():
    metadata = extract_video_metadata(VIDEO_MP4_PATH)
    print(f"{metadata=}")


if __name__ == "__main__":
    main()
