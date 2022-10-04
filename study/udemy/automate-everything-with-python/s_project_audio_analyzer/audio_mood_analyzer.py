from pathlib import Path
from q_nlp.nlp import has_positive_sentiment
from x_audio_processing.audio_recognition import audio_to_text

from s_project_audio_analyzer.constants import AUDIO_FILE_PATH


def audio_mood_analyzed(audio_path: Path) -> str:
    if extracted_text := audio_to_text(audio_path):
        if has_positive_sentiment(extracted_text):
            return "Very good mood :D"
        else:
            return "Meh things are not that good :("
    else:
        return "Could not extract speech from audio provided."


def main():
    print(f"{audio_mood_analyzed(AUDIO_FILE_PATH)=}")


if __name__ == "__main__":
    main()
