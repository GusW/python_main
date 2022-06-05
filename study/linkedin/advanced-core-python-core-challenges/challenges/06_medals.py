from collections import namedtuple

with open("olympics.txt", "rt", encoding="utf-8") as file:
    olympics = file.read()

medal = namedtuple(
    "medal",
    [
        "City",
        "Edition",
        "Sport",
        "Discipline",
        "Athlete",
        "NOC",
        "Gender",
        "Event",
        "Event_gender",
        "Medal",
    ],
)

medals = []  # Complete this - medals is a list of medal namedtuples


def get_medals(**kwargs):
    """Return a list of medal namedtuples"""
    res = []
    for row in olympics.splitlines()[1:]:
        m = medal(*row.split(";"))
        if all(getattr(m, k) == v for k, v in kwargs.items()):
            res.append(m)

    return res


if __name__ == "__main__":
    expected = [
        medal(
            City="Los Angeles",
            Edition="1984",
            Sport="Athletics",
            Discipline="Athletics",
            Athlete="LEWIS, Carl",
            NOC="USA",
            Gender="Men",
            Event="100m",
            Event_gender="M",
            Medal="Gold",
        ),
        medal(
            City="Seoul",
            Edition="1988",
            Sport="Athletics",
            Discipline="Athletics",
            Athlete="LEWIS, Carl",
            NOC="USA",
            Gender="Men",
            Event="100m",
            Event_gender="M",
            Medal="Gold",
        ),
    ]
    actual = get_medals(Athlete="LEWIS, Carl", Event="100m")
    assert actual == expected

    expected = []
    actual = get_medals(Athlete="FERNANDES, Jonathan")
    assert actual == expected

    expected = 1459
    actual = len(get_medals(Edition="1984"))
    assert actual == expected
