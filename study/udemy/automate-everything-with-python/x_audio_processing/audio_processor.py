from pathlib import Path
from typing import Union

from pydub import AudioSegment

from x_audio_processing.constants import TEMP_FOLDER_PATH


def load_wav(audio_path: Path, volume_gain: int = 0) -> AudioSegment:
    try:
        return AudioSegment.from_wav(audio_path) + volume_gain
    except Exception as err:
        print(f"!!!ERROR!!! Could not load audio: {err}")


def save_audio(audio: AudioSegment, destination_path: Path) -> None:
    try:
        audio.export(destination_path.as_posix())
        print(f"{destination_path.name} saved.")
    except Exception as err:
        print(f"!!!ERROR!!! Could not save audio: {err}")


def _handle_audio_obj_or_path(
    original_audio: Union[AudioSegment, Path]
) -> AudioSegment:
    return (
        original_audio
        if isinstance(original_audio, AudioSegment)
        else load_wav(original_audio)
    )


def reverse_audio(original_audio: Union[AudioSegment, Path]) -> AudioSegment:
    try:
        audio = _handle_audio_obj_or_path(original_audio)
        return audio.reverse()
    except Exception as err:
        print(f"!!!ERROR!!! Could not reverse audio: {err}")


def slice_audio(
    original_audio: Union[AudioSegment, Path], from_ms: int = 0, to_ms: int = 1000
) -> AudioSegment:
    audio = _handle_audio_obj_or_path(original_audio)
    to_ms = to_ms + 1
    return audio[from_ms:to_ms]


def audio_length_ms(original_audio: Union[AudioSegment, Path]) -> int:
    audio = _handle_audio_obj_or_path(original_audio)
    return len(audio)


def low_pass_filter(
    original_audio: Union[AudioSegment, Path], cutoff: int = 2000
) -> AudioSegment:
    audio = _handle_audio_obj_or_path(original_audio)
    return audio.low_pass_filter(cutoff)


def cue_channel(original_audio: Union[AudioSegment, Path], channel: float = 0.0):
    """
    left: -1
    right: 1
    both: 0
    """
    audio = _handle_audio_obj_or_path(original_audio)
    return audio.pan(channel)


def merge_audio(
    original_audio_1: Union[AudioSegment, Path],
    original_audio_2: Union[AudioSegment, Path],
    silent_ms: int = 0,
):
    first_audio = _handle_audio_obj_or_path(original_audio_1)
    second_audio = _handle_audio_obj_or_path(original_audio_2)
    return first_audio + AudioSegment.silent(silent_ms) + second_audio


def mix(
    original_audio_1: Union[AudioSegment, Path],
    original_audio_2: Union[AudioSegment, Path],
) -> AudioSegment:
    first_audio = _handle_audio_obj_or_path(original_audio_1)
    second_audio = _handle_audio_obj_or_path(original_audio_2)
    return first_audio.overlay(second_audio)


def main():
    beat_path = Path.joinpath(TEMP_FOLDER_PATH, "beat.wav")

    reversed_audio = reverse_audio(beat_path)
    save_audio(reversed_audio, Path.joinpath(TEMP_FOLDER_PATH, "beat_reversed.wav"))

    sliced_audio = slice_audio(beat_path, to_ms=2000)
    save_audio(sliced_audio, Path.joinpath(TEMP_FOLDER_PATH, "beat_sliced.wav"))

    merged_audio = merge_audio(beat_path, beat_path, silent_ms=50)
    save_audio(merged_audio, Path.joinpath(TEMP_FOLDER_PATH, "beat_merged.wav"))

    higher_volume_audio = load_wav(beat_path, volume_gain=18)
    save_audio(
        higher_volume_audio, Path.joinpath(TEMP_FOLDER_PATH, "beat_volume_up.wav")
    )

    double_beat = merge_audio(beat_path, beat_path)
    mixed_audio = mix(double_beat, Path.joinpath(TEMP_FOLDER_PATH, "sax.wav"))
    save_audio(mixed_audio, Path.joinpath(TEMP_FOLDER_PATH, "beat_mixed.wav"))

    beat_left = cue_channel(beat_path, -1)
    beat_right = cue_channel(beat_path, 1)
    beat_low = low_pass_filter(beat_path, cutoff=2500)
    beat_final = beat_left + beat_right + beat_low
    save_audio(beat_final, Path.joinpath(TEMP_FOLDER_PATH, "beat_final.wav"))


if __name__ == "__main__":
    main()
