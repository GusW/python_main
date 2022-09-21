import json

import requests


url = "https://api.languagetool.org/v2/check"
data = {"text": "Tis is a nixe day", "language": "auto"}

if __name__ == "__main__":
    res = requests.post(url, data=data)
    print(json.loads(res.text))
