"""
Python Descriptors
"""
from functools import cache

from typing import Any


class Descriptor:
    """
    Descriptors class
    """
    def __init__(self) -> None:
        self.__bmi = 0

    def __get__(self, instance: Any, owner: Any) -> int:
        return self.__bmi

    def __set__(self, instance: Any, value: int):
        if not isinstance(value, int):
            raise TypeError(f"{instance} should be set as type INT; received {type(value)}")

        if value < 0:
            raise ValueError(f'BMI cannot be negative; received {value}')

        self.__bmi = value

    def __delete__(self, instance: Any):
        del self.__bmi


class Person:
    """
    Person class
    """
    bmi = Descriptor()
    def __init__(self, name: str, age: int, bmi: int | float) -> None:
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self) -> str:
        return f"{self.name} age is {self.age} with a bmi of {self.bmi}"


class PersonName:
    """
    PersonName class
    """
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        """instance get_name method"""
        return self._name

    def set_name(self, new_name: str) -> None:
        """instance set_name method"""
        self._name = new_name

    def del_name(self) -> None:
        """instance del_name method"""
        del self._name

    name = property(get_name, set_name, del_name)


if __name__ == "__main__":
    joe = Person("Joe", 25, 17)
    print(f"{str(joe)=}\n")

    # throws ValueError
    # john = Person("John", 25, -5)
    # also throws ValueError
    # joe.bmi = -890

    john = PersonName('John')
    print(f"{str(john.name)=}\n")

    john.name = 'Joseph'
    print(f"{str(john.name)=}\n")

    del john.name
    print(f"{str(vars(john))=}\n")
