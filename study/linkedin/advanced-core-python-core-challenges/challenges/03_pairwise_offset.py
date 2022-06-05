from itertools import tee, zip_longest, chain


def pairwise_offset(sequence, fillvalue="*", offset=0):
    target = [fillvalue] * offset
    left_arr = list(sequence)
    left_arr.extend(target)
    right_arr = [*target]
    right_arr.extend(sequence)
    return [(left, right) for left, right in zip(left_arr, right_arr)]


def pairwise_offset_v2(sequence, fillvalue="*", offset=0):
    """Using itertools"""
    it1, it2 = tee(sequence, 2)
    return zip_longest(it1, chain(fillvalue * offset, it2), fillvalue=fillvalue)


if __name__ == "__main__":

    actual = list(pairwise_offset("abcde"))
    expected = [("a", "a"), ("b", "b"), ("c", "c"), ("d", "d"), ("e", "e")]
    assert expected == actual

    actual = list(pairwise_offset("abcd", fillvalue="-", offset=1))
    expected = [("a", "-"), ("b", "a"), ("c", "b"), ("d", "c"), ("-", "d")]
    assert expected == actual

    actual = list(pairwise_offset([(1, 2), (3, 4), (5, 6)], offset=2))
    expected = [
        ((1, 2), "*"),
        ((3, 4), "*"),
        ((5, 6), (1, 2)),
        ("*", (3, 4)),
        ("*", (5, 6)),
    ]
    assert expected == actual

    actual = list(pairwise_offset([(1, 2), (3, 4), (5, 6)], offset=4))
    expected = [
        ((1, 2), "*"),
        ((3, 4), "*"),
        ((5, 6), "*"),
        ("*", "*"),
        ("*", (1, 2)),
        ("*", (3, 4)),
        ("*", (5, 6)),
    ]
    assert expected == actual
