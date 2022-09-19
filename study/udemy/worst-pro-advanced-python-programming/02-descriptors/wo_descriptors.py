"""
Python Descriptors
"""


class Person:
    """
    Person class
    """
    def __init__(self, name: str, age: int, bmi: int | float) -> None:
        self.name = name
        self.age = age
        self.bmi = self._handle_bmi(bmi)

    def _handle_bmi(self, bmi: int | float) -> Exception | float | int:
        if bmi < 0:
            raise ValueError(f'BMI cannot be negative; received {bmi}')

        return bmi


    def __str__(self) -> str:
        return f"{self.name} age is {self.age} with a bmi of {self.bmi}"


if __name__ == "__main__":
    joe = Person("Joe", 25, 17)
    print(f"{str(joe)=}\n")

    # throws ValueError
    # john = Person("John", 25, -5)

    # does no throw ValueError
    joe.bmi = -890
    print(f"{str(joe)=}\n")
