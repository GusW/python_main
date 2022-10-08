from pathlib import Path

import sounddevice
from scipy.io.wavfile import write

from z_audio_mouse_keyboard.constants import TEMP_FOLDER_PATH


def record_audio(sample_rate: int, seconds: int, output_path: Path):
    try:
        audio = sounddevice.rec(
            frames=seconds * sample_rate, samplerate=sample_rate, channels=1
        )
        sounddevice.wait()
        write(output_path, sample_rate, audio)
    except Exception as err:
        print(f"!!!ERROR!!! {err}")


def main():
    seconds = 5
    sample_rate = 44100  # fps, Hz
    record_audio(sample_rate, seconds, TEMP_FOLDER_PATH.joinpath("output.mp3"))


if __name__ == "__main__":
    main()
