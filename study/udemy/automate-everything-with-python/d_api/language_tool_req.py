import json

import requests

from d_api.constants import LANGUAGE_TOOL_CHECK_ENDPOINT


def check_spelling(text: str, language: str = "auto"):
    data = {"text": text, "language": language}
    res = requests.post(LANGUAGE_TOOL_CHECK_ENDPOINT, data=data)
    return json.loads(res.text)


if __name__ == "__main__":
    text = "Tis is a nixe day"
    print(check_spelling(text))
