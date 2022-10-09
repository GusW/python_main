from enum import Enum
from functools import cache
from typing import Optional

from googletrans import Translator


class Languages(str, Enum):
    ENGLISH = "en"


@cache
def get_translator():
    return Translator()


def translate(
    text: str, destination_language: Languages = Languages.ENGLISH
) -> Optional[str]:
    try:
        translator = get_translator()
        translation = translator.translate(text, dest=destination_language)
        return translation.text if translation else ""
    except Exception as err:
        print(f"!!!ERROR!!! {err}")


def main():
    print(f"{translate('Oa mai oe?')=}")


if __name__ == "__main__":
    main()
