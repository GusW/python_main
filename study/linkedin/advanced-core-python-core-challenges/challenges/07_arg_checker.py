from functools import wraps
import pytest


def arg_checker(*arg_types):
    """An argument checker decorator that checks both:
     - The number of variables that you use for a function
     - The type of each variable.
    Raises a TypeError if either of these fail"""

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if (expected_len := len(arg_types)) != (arg_len := len(args)):
                raise TypeError(
                    f"Expected {expected_len} arguments, received {arg_len}"
                )

            if mismatches := [
                f"Argument {ar} should be type {ar_type}, received {type(ar)}"
                for ar, ar_type in zip(args, arg_types)
                if not isinstance(ar, ar_type)
            ]:
                raise TypeError("\n".join(mismatches))

            return function(*args, **kwargs)

        return wrapper

    return decorator


@arg_checker(int, int, int)
def adder(a: int, b: int, c: int):
    """Returns the sum of the arguments"""
    # deepcode ignore addOfStringAndNonString: <please specify a reason of ignoring this>
    return a + b + c


if __name__ == "__main__":

    assert adder(1, 2, 3) == 6

    with pytest.raises(TypeError):
        adder(1, 2)
        # deepcode ignore WrongNumberOfArguments: <please specify a reason of ignoring this>
        adder(1, 2, 3, 4)

    with pytest.raises(TypeError):
        adder("1", 2, 3)
        adder(1, 2.0, 3)
        adder(1, 2, "3")

    assert adder.__name__ == "adder"
    assert adder.__doc__ == "Returns the sum of the arguments"
