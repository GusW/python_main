import pytest


class Calculator:
    def __init__(self):
        self.exc_types = (TypeError, ValueError, NameError, ZeroDivisionError)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.error = exc_value
        return isinstance(exc_value, self.exc_types)


if __name__ == "__main__":

    with Calculator() as c:
        print(1 * 2)
        print(2 / 3)
        print(3 + 4)
    assert c.error is None

    with pytest.raises(ZeroDivisionError):
        with Calculator() as c:
            print(1 * 2)
            print(2 / 0)
            print(3 + 4)
        raise c.error

    with pytest.raises(TypeError):
        with Calculator() as c:
            print(1 * 2)
            print(2 + "2")
            print(3 + 4)
        raise c.error

    with pytest.raises(ValueError):
        with Calculator() as c:
            print(1 * 2)
            print(2 + int("a"))
            print(3 + 4)
        raise c.error

    with pytest.raises(NameError):
        with Calculator() as c:
            print(1 * 2)
            print(2 / num)
            print(3 + 4)
        raise c.error
