from functools import cache

from gspread import service_account

from k_google_sheets.constants import GOOGLE_SECRETS_PATH


@cache
def get_gs():
    return service_account(GOOGLE_SECRETS_PATH)
