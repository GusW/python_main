'''
Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single
point of access to it for any other code.
Singleton has almost the same pros and cons as global variables. Although they’re super-handy,
they break the modularity of your code.
You can’t just use a class that depends on Singleton in some other context.
You’ll have to carry the Singleton class as well.
Most of the time, this limitation comes up during the creation of unit tests.
'''


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self) -> None:
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        print(f'Hello there I am id {id(self)}!')


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    s1.some_business_logic()
    s2.some_business_logic()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
