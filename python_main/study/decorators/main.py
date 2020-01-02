from datetime import datetime


def get_function():
    print "inside get_function"

    def returned_function():
        print "inside returned_function"
        return 1
    print "outside returned_function"
    return returned_function


def timed_event(func):
    def new_function(*args, **kwargs):
        before = datetime.now()
        x = func(*args, **kwargs)
        after = datetime.now()
        print("Elapsed time: {}".format(
            after-before
        ))
        return x
    return new_function

@timed_event
def add(x, y):
    return x + y


@timed_event
def multiply(x, y):
    return x * y

