from collections import namedtuple
from pathlib import Path
import pytest
import re

PARENT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = Path.joinpath(PARENT_PATH, "data", "specifications.txt")

with open(DATA_PATH, "rt") as file:
    specifications = file.read()

specs = namedtuple("specs", "range regex")
# specs range builtin module
# specs regex from re.compile


def get_linkedin_dict():
    """Convert specifications into a dict:
    keys:  feature
    values: specs namedtuple"""
    data = {}
    minimum, maximum = 0, 0
    regex = ""
    for line in specifications.splitlines():
        if line:
            if "requirements" in line:
                minimum, maximum = re.findall(r"\d+", line)
                minimum = int(minimum)
                maximum = int(maximum)
            elif "permitted characters" in line:
                regex = "".join(line.split()[2:])
                regex = re.compile(rf"^[{regex}]+$")
            elif "login characters" in line:
                regex = "".join(line.split()[2:])
                regex = regex[::-1]
                regex = regex.replace(".", ".\\", 1).replace("-", "-\\", 1)
                regex = regex[::-1]
                regex = re.compile(rf"^[{regex}]+@[{regex}]+.com|net|org$")
            else:
                feature = line.split()[-1]
            data[feature] = specs(range(minimum, maximum + 1), regex)
    return data


def check_linkedin_feature(feature_text, url_or_login):
    """Raise a ValueError if the url_or_login isn't login or custom_url
    If feature_text is valid, return True otherwise return False"""
    data = get_linkedin_dict()
    result = data.get(url_or_login, None)
    if result is None:
        raise ValueError("Feature needs to be either login or custom_url")
    else:
        length = len(feature_text) in data[url_or_login].range
        regex = bool(data[url_or_login].regex.search(feature_text))
        return length & regex


if __name__ == "__main__":
    assert check_linkedin_feature("jonathanafernandes", "custom_url")
    assert check_linkedin_feature("jonfernandes2000", "custom_url")
    assert check_linkedin_feature("JonathanFernandes", "custom_url")
    assert check_linkedin_feature("JonathanFernandes2000", "custom_url")

    assert not check_linkedin_feature("jonathanafernande$", "custom_url")
    assert not check_linkedin_feature("jon-fernandes2000", "custom_url")
    assert not check_linkedin_feature("Jonathan_Fernandes", "custom_url")
    assert not check_linkedin_feature("JonathanFernandes2000!!", "custom_url")

    assert check_linkedin_feature("jf@gmail.com", "login")
    assert check_linkedin_feature("jonathanfernandes@gmail.com", "login")
    assert check_linkedin_feature("jonathan-fernandes@gmail.com", "login")
    assert check_linkedin_feature("jonathan_fernandes@gmail.com", "login")
    assert check_linkedin_feature("jonathan.fernandes@gmail.com", "login")

    assert not check_linkedin_feature("jonathangmail.com", "login")
    assert not check_linkedin_feature("jonathanfernandes@gmail.biz", "login")
    assert not check_linkedin_feature("jonathanfernandes@gmail.co.uk", "login")

    with pytest.raises(ValueError):
        assert check_linkedin_feature("jonathanafernandes", "www")
        assert check_linkedin_feature("jonathanafernandes", "webpage")
        assert check_linkedin_feature("jonathanafernandes", "social")
