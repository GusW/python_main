from pathlib import Path, PosixPath

from cv2 import (
    VideoCapture,
    VideoWriter,
    VideoWriter_fourcc,
    imshow,
    waitKey,
    destroyAllWindows,
)

from l_image_processing.detect_faces import detect_faces
from m_video_processing.constants import TEMP_FOLDER_PATH


def create_camera_frame():
    video = VideoCapture(0)  # int 0: main device camera; 1, 2...
    success, frame = video.read()
    while True:
        success, frame = video.read()
        if not success:
            break

        # visual feedback
        imshow("Instant camera access...", frame)

        if (key := waitKey(1)) and key == ord("q"):
            break

    video.release()
    destroyAllWindows()


def create_webcam_with_face_detector(output_path: PosixPath):
    video = VideoCapture(0)  # int 0: main device camera; 1, 2...

    success, frame = video.read()
    height = frame.shape[0]
    width = frame.shape[1]

    output = VideoWriter(
        Path.joinpath(output_path, "webcam_with_face_detection.avi").as_posix(),
        VideoWriter_fourcc(*"DIVX"),
        15,
        (width, height),
    )

    count = 0
    while True:
        success, frame = video.read()
        if not success:
            break

        count += 1
        mod_frame = detect_faces(frame, "webcam")

        # visual feedback
        imshow("Recording webcam...", mod_frame)

        if (key := waitKey(1)) and key == ord("q"):
            break

        output.write(mod_frame)
        print(f"Processing frame {count}...")

    output.release()
    video.release()
    destroyAllWindows()


def main():
    # create_camera_frame()
    create_webcam_with_face_detector(TEMP_FOLDER_PATH)


if __name__ == "__main__":
    main()
