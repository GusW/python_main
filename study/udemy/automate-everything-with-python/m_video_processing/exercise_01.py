from datetime import datetime

from m_video_processing.constants import EXERCISE_01_PATH, VIDEO_MP4_PATH

from m_video_processing.extract_video_frames import extract_video_frames
from m_video_processing.extract_video_metadata import extract_video_metadata


def main():
    target_timestamp = "00:00:02.75"
    target_dt = datetime.strptime(target_timestamp, "%H:%M:%S.%f")

    video_metadata = extract_video_metadata(VIDEO_MP4_PATH)

    target_frame = video_metadata.get("fps", 0) * (
        target_dt.hour * 3600
        + target_dt.minute * 60
        + target_dt.second
        + target_dt.microsecond / 10**6
    )
    if 0 < target_frame <= video_metadata.get("frame_count", 0):
        extract_video_frames(
            VIDEO_MP4_PATH, EXERCISE_01_PATH, target_frame=int(target_frame)
        )


if __name__ == "__main__":
    main()
