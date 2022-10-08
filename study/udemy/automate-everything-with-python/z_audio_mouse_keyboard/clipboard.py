import pyperclip
import pyautogui


def peek_clipboard():
    last_clipboard = pyperclip.paste()
    pyautogui.alert(last_clipboard)
    print(f"{last_clipboard=}")


def main():
    peek_clipboard()


if __name__ == "__main__":
    main()
