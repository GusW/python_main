from pathlib import Path
from typing import Optional

from speech_recognition import Recognizer, AudioFile

from x_audio_processing.constants import TEMP_FOLDER_PATH

recognizer = Recognizer()


def audio_to_text(audio_path: Path) -> Optional[str]:
    try:
        with AudioFile(audio_path.as_posix()) as audio_file:
            audio = recognizer.record(audio_file)

        return recognizer.recognize_google(audio)
    except Exception as err:
        print(f"!!!ERROR!!! could not extract text from audio: {err}")


def main():
    text_from_audio = audio_to_text(Path.joinpath(TEMP_FOLDER_PATH, "chile.wav"))
    print(f"\n{text_from_audio=}\n")


if __name__ == "__main__":
    main()
