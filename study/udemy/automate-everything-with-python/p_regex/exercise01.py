import re
from typing import Optional


data = [
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com",
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants",
]

expected_delhi = [
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants",
]

expected_delhi_and_email = ["mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com"]

expected_delhi_and_phone_number = ["mrs Alma Stills Delhi 01231981 1 dog"]

expected_delhi_and_phone_number_or_address = [
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "mrs Alma Stills Delhi 01231981 1 dog",
]


def _find_all_with_delhi_exp(entries: list[Optional[str]]):
    regex = re.compile(r"delhi", re.IGNORECASE)
    return [entry for entry in entries if regex.findall(entry)]


def _find_all_with_delhi_and_email(entries: list[Optional[str]]):
    regex = re.compile(r"delhi.*[^ ]+@[^ ]+\.[a-z]+", re.IGNORECASE)
    return [entry for entry in entries if regex.findall(entry)]


def _find_all_with_delhi_and_phone_number(entries: list[Optional[str]]):
    # assuming phone numbers start with either + or 0 and have from 7 to 20 digits
    regex = re.compile(r"delhi.*[+|0][0-9]{7,20}", re.IGNORECASE)
    return [entry for entry in entries if regex.findall(entry)]


def _find_all_with_delhi_and_phone_number_or_address(entries: list[Optional[str]]):
    regex = re.compile(
        r"delhi.*(?:[+|0][0-9]{7,20}|[^ ]+@[^ ]+\.[a-z]+)", re.IGNORECASE
    )
    return [entry for entry in entries if regex.findall(entry)]


def main() -> list[Optional[str]]:
    assert _find_all_with_delhi_exp(data) == expected_delhi
    assert _find_all_with_delhi_and_email(data) == expected_delhi_and_email
    assert (
        _find_all_with_delhi_and_phone_number(data) == expected_delhi_and_phone_number
    )
    assert (
        _find_all_with_delhi_and_phone_number_or_address(data)
        == expected_delhi_and_phone_number_or_address
    )


if __name__ == "__main__":
    main()
