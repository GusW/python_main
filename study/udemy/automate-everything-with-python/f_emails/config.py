from functools import cache
import smtplib

import yagmail

from f_emails.constants import (
    GMAIL_SENDER_EMAIL,
    GMAIL_SENDER_PW,
    OUTLOOK_SENDER_EMAIL,
    OUTLOOK_SENDER_PW,
    OUTLOOK_SMTP_SERVER,
    OUTLOOK_SMTP_PORT,
)


@cache
def gmail_client() -> yagmail.SMTP:
    return yagmail.SMTP(user=GMAIL_SENDER_EMAIL, password=GMAIL_SENDER_PW)


# @cache
def _outlook_server():
    server = smtplib.SMTP(OUTLOOK_SMTP_SERVER, OUTLOOK_SMTP_PORT)
    server.starttls()
    server.login(OUTLOOK_SENDER_EMAIL, OUTLOOK_SENDER_PW)
    return server


def outlook_send_email(receiver: str, message=""):
    server = _outlook_server()
    server.sendmail(OUTLOOK_SENDER_EMAIL, receiver, message)
    server.quit()
    print("Outlook email sent!")
