from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from pathlib import Path

from f_emails.config import outlook_send_email
from f_emails.constants import RECEIVER, OUTLOOK_SENDER_EMAIL, ATTACHMENT_PATH


def send_plain_text_email(receiver: str, message: str = ""):
    outlook_send_email(receiver, message=message)


def send_html_email(
    receiver: str, subject: str = "", contents: str = "", attachment: MIMEBase = None
):
    body = f"""
    <h2>Hi there {receiver}!</h2>
    </br>
    <h3>{contents}</h3>
    """
    mimetext = MIMEText(body, "html")

    message = MIMEMultipart()
    message["From"] = OUTLOOK_SENDER_EMAIL
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(mimetext)
    if attachment:
        message.attach(attachment)

    outlook_send_email(receiver, message=message.as_string())


def create_attachment_payload(attachment_path: Path):
    attachment_file = open(attachment_path, "rb")
    payload = MIMEBase("application", "octate-stream")
    payload.set_payload(attachment_file.read())
    encoders.encode_base64(payload)

    payload.add_header(
        "Content-Disposition", "attachment", filename=attachment_path.name
    )
    return payload


def main():
    # plain text

    message = """
    Subject: Hello from Python

    Hello from Python in Outlook!
    """
    send_plain_text_email(RECEIVER, message=message)

    # plain text
    # html

    send_html_email(
        RECEIVER,
        subject="Hello again from Python",
        contents="Here we come again sending enriched emails from Python",
    )

    # html
    # attachment

    attachment = create_attachment_payload(ATTACHMENT_PATH)
    send_html_email(
        RECEIVER,
        subject="Python is sending a file",
        contents="You should have received a file attached by Python.",
        attachment=attachment,
    )

    # attachment


if __name__ == "__main__":
    main()
