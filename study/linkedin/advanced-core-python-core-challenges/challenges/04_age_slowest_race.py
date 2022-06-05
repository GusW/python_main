# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
import re
from datetime import datetime
from pathlib import Path


ROOT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = Path.joinpath(ROOT_PATH, "data", "10k_racetimes.txt")
ATHELETE_NAME = "Jennifer Rhines"


def get_data():
    with open(DATA_PATH, "rt") as file:
        content = file.read()
    return content


def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt,
    parse it and return a tuple of (age at event, race time).
    Assume a year has 365.25 days"""
    time = re.findall(r"\d{2}:\S+", line)[0]
    dates = re.findall(r"\d{2}\s\w{3}\s\d{4}", line)
    if time and len(dates) == 2:
        race_date, dob = dates
        race_date = datetime.strptime(race_date, "%d %b %Y")
        dob = datetime.strptime(dob, "%d %b %Y")
        years, days = divmod((race_date - dob).days, 365.25)
        return (f"{int(years)}y{int(days)}d", time)
    else:
        raise Exception(
            f"Could not find all athlete information:\ntime: {time}\nrace_date: {race_date}\nDoB: {dob}"
        )


def get_age_slowest_times():
    """Return a tuple (age, race_time) where:
    age: AyBd is in this format where A and B are integers"""
    return max(
        [
            get_event_time(row)
            for row in get_data().splitlines()
            if ATHELETE_NAME in row
        ],
        key=lambda x: x[1],
    )


if __name__ == "__main__":
    expected = "40y67d"
    result = get_age_slowest_times()[0]
    assert expected == result

    expected = "33:31"
    result = get_age_slowest_times()[1]
    assert expected == result
