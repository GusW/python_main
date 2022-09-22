import pandas as pd

from f_emails.config import gmail_client
from f_emails.constants import CONTACTS_PATH, ATTACHMENT_PATH, RECEIVER


def send_email(receiver: str, subject: str = "", contents: str = "") -> None:
    gmail_client().send(to=receiver, subject=subject, contents=contents)
    print("Email sent!")


def send_email_to_list(
    contacts: list[str], subject: str = "", contents: str = ""
) -> None:
    for email in contacts:
        send_email(email, subject=subject, contents=contents)


def send_email_with_attachment(
    receiver: str, subject: str = "", contents: str = "", file_path: str = ""
):
    gmail_client().send(to=receiver, subject=subject, contents=[contents, file_path])
    print("Email with attachment was sent!")


def main() -> None:
    subject = "Hello from Python!"
    contents = """
    Hey!
    I'm sending this email using Python.
    """
    # send_email
    send_email(RECEIVER, subject=subject, contents=contents)
    # send_email

    # send_email_to_list
    df = pd.read_csv(CONTACTS_PATH)
    contacts = [row.get("email") for _, row in df.iterrows()]
    send_email_to_list(
        contacts, subject=f"Distribution List: {subject}", contents=contents
    )
    # send_email_to_list

    # send_email_with_attachment
    send_email_with_attachment(
        RECEIVER,
        subject=f"Attachment: {subject}",
        contents=contents,
        file_path=ATTACHMENT_PATH.as_posix(),
    )
    # send_email_with_attachment


if __name__ == "__main__":
    main()
