from time import sleep

from f_emails.constants import RECEIVER
from f_emails.send_gmail_email import send_email


def schedule_email(
    time_in_seconds: int, receiver: str, subject: str = "", contents: str = ""
) -> None:
    while True:
        send_email(receiver, subject=subject, contents=contents)
        sleep(time_in_seconds)


def main() -> None:
    subject = "Hello from Python!"
    contents = """
    Hey!
    I'm sending this email using Python.
    """
    schedule_email(60, RECEIVER, subject=subject, contents=contents)


if __name__ == "__main__":
    main()
