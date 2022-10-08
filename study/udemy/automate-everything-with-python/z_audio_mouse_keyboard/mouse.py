from typing import Optional

import pyautogui


def get_mouse_position() -> tuple[int, int]:
    return pyautogui.position()


def move_mouse_to_absolute(x: int, y: int, duration: Optional[float] = 0.0) -> None:
    pyautogui.moveTo(x, y, duration=duration)


def move_mouse_relative(x: int, y: int, duration: Optional[float] = 0.0) -> None:
    pyautogui.move(x, y, duration=duration)


def mouse_click(is_double_click: bool = False, is_right_click: bool = False) -> None:
    if is_double_click:
        pyautogui.doubleClick()
    else:
        # pyautogui.click(button="right" if is_right_click else "left") WINDOWS
        pyautogui.click()
        pyautogui.dragTo(button="right" if is_right_click else "left")


def mouse_click_on_coordinates(x: int, y: int) -> None:
    pyautogui.click(x, y)


def mouse_drag(
    to_x: int, to_y: int, duration: Optional[float] = 0.0, is_absolute: bool = True
):
    if is_absolute:
        pyautogui.dragTo(to_x, to_y, duration=duration)
    else:
        pyautogui.drag(to_x, to_y, duration=duration)


def draw(start_x: int, start_y: int, end_x: int, end_y: int):
    """
    Depends on the operating system and drawing application
    example: https://jspaint.app
    """
    move_mouse_to_absolute(start_x, start_y, duration=0.5)
    mouse_click()
    mouse_drag(end_x, end_y, duration=0.5)


def main():
    print(f"{get_mouse_position()=}")


if __name__ == "__main__":
    main()
