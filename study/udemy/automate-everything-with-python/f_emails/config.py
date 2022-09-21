from functools import cache

import yagmail

from f_emails.constants import SENDER_EMAIL, SENDER_PW


@cache
def email_client() -> yagmail.SMTP:
    return yagmail.SMTP(user=SENDER_EMAIL, password=SENDER_PW)
