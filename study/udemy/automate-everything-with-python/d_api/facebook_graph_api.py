import requests

from d_api.constants import FACEBOOK_TOKEN, FACEBOOK_STANDARD_ID


def _generate_graph_api_url(
    resource_id: str = FACEBOOK_STANDARD_ID, fields: list[str] = ["id", "name", "posts"]
):
    return f"https://graph.facebook.com/v15.0/{resource_id}?fields={'%2C'.join(fields)}&access_token={FACEBOOK_TOKEN}"


if __name__ == "__main__":
    url = _generate_graph_api_url(fields=["posts"])
    res = requests.get(url)
    print(res.text)
