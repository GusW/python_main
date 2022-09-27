from m_video_processing.detect_faces import create_video_with_face_detector
from n_censor_faces.constants import SMILE_VIDEO_PATH, CAT_FILE_PATH, TEMP_FOLDER_PATH


def main():
    create_video_with_face_detector(
        SMILE_VIDEO_PATH,
        TEMP_FOLDER_PATH,
        file_name="smile_censored_with_cat.avi",
        pattern=CAT_FILE_PATH,
    )

    create_video_with_face_detector(
        SMILE_VIDEO_PATH,
        TEMP_FOLDER_PATH,
        file_name="smile_censored_with_blur.avi",
        is_blur=True,
    )

    create_video_with_face_detector(
        SMILE_VIDEO_PATH,
        TEMP_FOLDER_PATH,
        file_name="smile_censored_with_filled_rectangle.avi",
        is_filled_rectangle=True,
    )


if __name__ == "__main__":
    main()
