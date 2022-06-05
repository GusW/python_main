# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
import re
import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = Path.joinpath(FILE_PATH, "data", "10k_racetimes.txt")
TARGET_ATHLETE = "Jennifer Rhines"


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open(DATA_PATH, "rt") as file:
        content = file.read()
    return content


def _get_time_in_ms(stringyfied_time):
    minutes, seconds, ms = (
        list(map(int, re.split(r"[:.]", stringyfied_time)))
        if len(stringyfied_time) > 5
        else list(map(int, re.split(r"[:]", stringyfied_time))) + [0]
    )
    return ms + seconds * 1000 + minutes * 1000 * 60


def _get_time(line):
    return re.findall(r"\d{2}:\S+", line)[0]


def get_rhines_times(target_athlete=TARGET_ATHLETE):
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    return [row[3:14].strip() for row in races.splitlines() if target_athlete in row]


def get_average():
    """Return Jennifer Rhines' average race time in the format:
    mm:ss:M where :
    m corresponds to a minutes digit
    s corresponds to a seconds digit
    M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = [_get_time_in_ms(rt) for rt in get_rhines_times()]
    average = sum(racetimes) / len(racetimes)
    minutes = int(average // (1000 * 60))
    average -= minutes * 1000 * 60
    seconds = int(average // 1000)
    ms = int(average - seconds * 1000) // 100
    return f"{minutes:02d}:{seconds:02d}.{ms}"


def get_average_v2():
    """Return Jennifer Rhines' average race time in the format:
    mm:ss:M where :
    m corresponds to a minutes digit
    s corresponds to a seconds digit
    M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for racetime in racetimes:
        try:
            mins, secs, ms = re.split(r"[:.]", racetime)
            total += datetime.timedelta(
                minutes=int(mins), seconds=int(secs), milliseconds=int(ms)
            )
        except ValueError:
            mins, secs = re.split(r"[:.]", racetime)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs))
    return f"{total / len(racetimes)}"[2:-5]


if __name__ == "__main__":
    result = get_rhines_times()
    expected = ["32:32.006", "33:04", "33:21", "33:25", "33:30", "33:31"]
    assert result == expected

    result = get_average()
    expected = "33:13.8"
    assert result == expected
