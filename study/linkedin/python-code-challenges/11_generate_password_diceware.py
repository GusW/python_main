import secrets
from pathlib import Path

_FOLDER_PATH = Path(__file__).parent.resolve()
_DATA_PATH = Path.joinpath(_FOLDER_PATH, "data", "diceware.wordlist.asc")


def generate_passphrase(num_words):
    with open(_DATA_PATH, "r") as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for _ in range(num_words)]
    return " ".join(words)


if __name__ == "__main__":
    print(generate_passphrase(7))
    print(generate_passphrase(7))
