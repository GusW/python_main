# -*- coding: utf-8 -*-
# args
# just need a * doesnt matter the name
# non-keyworded variable arguments
# args

# kwargs
# just need a ** doesnt matter the name
# keyworded variable arguments
# kwargs

# pdb
# from commandline
# python -m pdb test.py
#
# from inside the code
# import pdb, pdb.set_trace()
# pdb

# generators
# are iterators, but you can only iterate over them once.
# because they do not store all the values in memory
# they generate the values on the fly.
# generators are implemented as functions
# However, they do not return a value, they yield it
# Generators are best for calculating large sets of results

from contextlib import contextmanager
import itertools
from pprint import pprint
import inspect
from enum import Enum
from collections import namedtuple
from collections import deque
from collections import Counter
from collections import OrderedDict
import collections
import json
from collections import defaultdict
from functools import wraps
from datetime import datetime
from functools import reduce


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
# generators


# map
l = [2, 15, 13, 5, 66, 12, 29, 33]
max_sum = 0
for i in range(len(l)):
    s = sum(map(lambda x: x, list(map(lambda y: y, l[i: i+4]))))
    max_sum = s if s > max_sum else max_sum

print("max_sum map mode = {}".format(
    max_sum
))
# map

# reduce
for j in range(len(l)):
    s = reduce(lambda x, y: x + y, list(map(lambda y: y, l[j: j+4])))
    max_sum = s if s > max_sum else max_sum

print("max_sum reduce mode = {}".format(
    max_sum
))
# reduce

# filter
l2 = list(range(-3, 10))
r2 = list(filter(lambda x: x < 0, l2))
print('filtered list: {}'.format(
    r2
))
# filter

# set
# lists that they can not contain duplicate values
l3 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in l3 if l3.count(x) > 1])
print('duplicates are: {}'.format(
    list(duplicates)
))
#
# intersection
set1 = set(['yellow', 'red', 'blue', 'green', 'black'])
set2 = set(['red', 'brown'])
print('sets intersection: {}'.format(
    set2.intersection(set1),
))
#
# difference
set3 = set(['yellow', 'red', 'blue', 'green', 'black'])
set4 = set(['red', 'brown'])
print('sets difference: {}'.format(
    set4.difference(set3),
))
#
# creating sets
set5 = set(['red', 'blue', 'green'])
print('type of set5 is: {}'.format(
    type(set5)
))
# or
set6 = {'red', 'blue', 'green'}
print('type of set6 is: {}'.format(
    type(set6)
))
#
# set

# ternary operator
#condition_is_true if condition else condition_is_false
# ternary operator

# decorators
# function which recieves a function or a class as an argument
# and returns a function or a class as an argument


def decorator(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        begin = datetime.now()
        f = function(*args, **kwargs)
        end = datetime.now()
        print('Elapsed time was {}'.format(
            end-begin
        ))
        return f
    return decorated


def int_division_function(x, y):
    return x / y


int_division_function = decorator(int_division_function)
print(int_division_function(5, 2))


@decorator
def mod_division_function(x, y):
    return x % y
#
# decorators with args


def outer_decorator(*outer_args, **outer_kwargs):
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if (outer_kwargs['has_perms'] is not None and
                    outer_kwargs['has_perms'] == True):
                f = function(*args, **kwargs)

                return f
            else:
                print('no perms')

        return decorated
    return decorator


@outer_decorator(has_perms=True)
def has_perms_mod_function(x, y):
    return x % y


@outer_decorator(has_perms=False)
def no_perms_mod_function(x, y):
    return x % y
#
# class decorators
#
# decorators

# global & return
# Global variable can accessed outside the scope of the function


def global_profile():
    global name
    global age
    name = "Gustavo"
    age = 36


global_profile()
print('global name: {}'.format(
    name
))

print('global age: {}'.format(
    age
))
#
# return


def profile():
    name = "Marisa"
    age = 28
    return name, age


profile_name, profile_age = profile()
print('return name: {}'.format(profile_name))
print('return age: {}'.format(profile_age))
# global & return

# mutation
# mutable means ‘able to be changed’
# list, set, dict
# immutable means ‘constant’
# int, float, bool, str, tuple, unicode
# you assign a variable to another variable of mutable datatype
# any changes to the data are reflected by both variables
#


def add_to_mutable(num, target=[]):
    target.append(num)
    return target


print('mutable 1: {}'.format(add_to_mutable(1)))
print('mutable 2: {}'.format(add_to_mutable(2)))
print('mutable 3: {}'.format(add_to_mutable(3)))


def add_to_imutable(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target


print('imutable 1: {}'.format(add_to_imutable(1)))
print('imutable 2: {}'.format(add_to_imutable(2)))
print('imutable 3: {}'.format(add_to_imutable(3)))
# mutation

# slots
# every class have instance attributes
# stored in a class.__dict__
# however it uses a lot of RAM while creating thousands of objects
# __slots__ tell Python not to use a dict o
# only allocates space for a fixed set of attributes


class MyClassWOSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()


class MyClassWSlots(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
# slots

# virtualenv
# tool which allows us to make isolated python environments
# $ virtualenv myproject
# $ source myproject/bin/activate
# $ deactivate
# virtualenv


# collections
# defaultdict
# you do not need to check whether a key is present or not
colours1 = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favourite_colours = defaultdict(list)
for name, colour in colours1:
    favourite_colours[name].append(colour)

print(favourite_colours)


def tree(): return collections.defaultdict(tree)


some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(json.dumps(some_dict))
# defaultdict
# OrderedDict
# keeps its entries sorted as they are initially inserted
# Overwriting a value of an existing key doesn’t change the position of that key
colours = OrderedDict([("Red", 198),
                       ("Green", 170),
                       ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
# OrderedDict
# Counter
# allows us to count the occurrences of a particular item
favs = Counter(name for name, colour in colours1)
print(favs)
# Counter
# deque
# double ended queue
# append and delete elements from either side of the queue
d1 = deque(range(5))
print(len(d1))
d1.popleft()
d1.pop()
print(d1)
d1.extendleft([-10])
d1.extend([6, 7, 8])
print(d1)
# limit the amount of items a deque can hold
# when achieved the maximum limit of our deque it will simply pop out
# the items from the opposite end
d2 = deque(maxlen=30)
# deque
# namedtuple
# lists are mutable, tuples don't
# you can not reassign an item in a tuple
# namedtuples you don’t have to use integer indexes for accessing members of a tuple
# like dictionaries but unlike dictionaries they are immutable
Animal = namedtuple('Animal', 'name age type')
kitty = Animal(name="kitty", age=5, type="cat")
print(kitty)
print(kitty.name)
# you can convert a namedtuple to a dictionary
print(kitty._asdict())
# namedtuple
# enum.Enum (Python 3.4+)
# same thing as creating a class with specific enums


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
# enum.Enum (Python 3.4+)
# collections


# enumerate
# loop over something and have an automatic counter
my_list = ['apple', 'banana', 'grapes', 'pear']
# optional argument = where to start the index
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# enumerate

# object introspection
# introspection is the ability to determine the type of an object at runtime
# dir
# returns a list of attributes and methods belonging to an object
my_list = [1, 2, 3]
print(dir(my_list))
# dir
#### type and id
# type function returns the type of an object
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))
# id returns the unique ids of various objects
name = "gustavo"
print(id(name))
#### type and id
# inspect
# provides several useful functions to get information about live objects
print(inspect.getmembers(str))
# inspect
# object introspection

# comprehensions
# constructs that allow sequences to be built from other sequences
# list comprehensions
# short and concise way to create lists
# variable = [out_exp for out_exp in input_list if condition]
multiples_of_three = [i for i in range(30) if i % 3 == 0]
print(multiples_of_three)
# list comprehensions
# dict comprehensions
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)
# dict comprehensions
# set comprehensions
squared = {x**2 for x in [1, 2, 3, 4, 4]}
print(squared)
# set comprehensions
# comprehensions

# exceptions
# Handling multiple exceptions
# one-liner tuple
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
# multiple line
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred = {}".format(
        e
    ))
except IOError as e:
    print("An IO error occurred = {}".format(
        e
    ))
# one-liner handler
try:
    file = open('test.txt', 'rb')
except Exception as e:
    print("An error occurred = {}".format(
        e
    ))
# Handling multiple exceptions
# finally clause
# It might be used to perform clean-up after a script
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed always!")
# finally clause
# try/else clause
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. '
          'And an error here would NOT be caught.')
finally:
    print('This would be printed in every case.')
# try/else clause
# exceptions

# lambdas
# one line functions, also known as anonymous functions
# lambda argument: manipulate(argument)


def add(x, y): return x + y


print(add(3, 5))
# list sorting
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# lambdas

# one-liners
# Simple web server
# python -m SimpleHTTPServer (Python 2)
# python -m http.server (Python 3)
# Simple web server
# Pretty printing
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)
# Pretty printing
# Profiling a script
# helpful in pinpointing the bottlenecks in your scripts
# $ python -m cProfile my_script.py
# Profiling a script
# CSV to json
# python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
# CSV to json
# List flattening
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
# List flattening
# One-line class constructors


class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update(
            {k: v for k, v in locals().items() if k != 'self'})
# One-line class constructors
# one-liners


# For-else
# else clause executes when the loop completes normally
# the loop did not encounter any break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# For-else

# Python C extensions
# Python C extensions

# open function
# opens a file
# open function

# Targeting Python 2+3
# Targeting Python 2+3

# Coroutines
# generators are data producers
# coroutines are data consumers


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
#
search.close()
# Coroutines

# Function caching
# Function caching

# Context managers
# allow you to allocate and release resources precisely when you want to
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
# or
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
# implementing as a class


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
# Implementing a Context Manager as a Generator


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
# Context managers
