"""Using "timeit"""
from timeit import timeit

items = {
    "a": 1,
    "b": 2,
}
default = -1


def use_catch(key):
    """Use try/catch to get a key with default"""
    try:
        return items[key]
    except KeyError:
        return default


def use_get(key):
    """Use dict.get to get a key with default"""
    return items.get(key, default)


def time_it(function_name: str, arg_name: str):
    target_action = function_name.replace("use_", "")
    print(
        target_action,
        timeit(
            f'{function_name}("{arg_name}")', f"from __main__ import {function_name}"
        ),
    )


if __name__ == "__main__":
    # Key is in the dictionary
    time_it("use_catch", "a")
    time_it("use_get", "a")

    # Key is missing from the dictionary
    time_it("use_catch", "x")
    time_it("use_get", "x")
