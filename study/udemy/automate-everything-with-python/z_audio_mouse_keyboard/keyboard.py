from enum import Enum
from typing import Union

import pyautogui


class NonChars(str, Enum):
    BACKSPACE = "backspace"
    CTRL = "ctrl"
    DELETE = "delete"
    DOWN = "down"
    ENTER = "enter"
    LEFT = "left"
    RIGHT = "right"
    UP = "up"


def press_non_chars(non_char: NonChars) -> None:
    pyautogui.press(non_char)


def write(text: str) -> None:
    pyautogui.write(text)


def combination_of_keys(*args: Union[NonChars, str]):
    pyautogui.hotkey(args)


def main():
    press_non_chars(NonChars.ENTER)
    write("Hello World!\n")
    combination_of_keys(NonChars.CTRL, "a")


if __name__ == "__main__":
    main()
