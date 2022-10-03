from enum import Enum

import wikipedia
from q_nlp.nlp import find_similar_meaning
from q_nlp.constants import SENTENCES_SAMPLE_PATH

ANSWER_NOT_FOUND = (
    "Sorry, I do not have an answer for that. Would you like to try another question?"
)


class TextSources(Enum):
    LOCAL = 0
    WIKIPEDIA = 1


def _load_text_from_local_resources():
    with open(SENTENCES_SAMPLE_PATH, mode="r") as file_:
        return file_.read()


def _load_from_wikipedia():
    return wikipedia.page("Vegetables").content


def main(source: TextSources) -> None:
    text = (
        _load_from_wikipedia()
        if source == TextSources.WIKIPEDIA
        else _load_text_from_local_resources()
    )
    while True:
        if (
            question := input(
                "\nHi, what would you like to know today? Type 'quit' to exit\n"
            )
        ) == "quit":
            break

        print(find_similar_meaning(question, text) or ANSWER_NOT_FOUND)


if __name__ == "__main__":
    main(TextSources.WIKIPEDIA)
