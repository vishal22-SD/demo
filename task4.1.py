#abstraction in python
from abc import ABC, abstractmethod
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
r = K()
r.rk()

#abstraction using abstract method

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()

#polymorphism
def add(x, y, z=0):
    return x + y + z
print(add(2, 3))
print(add(2, 3, 4))

#encapsulation in python

class Base:
    def __init__(self):
        self.a = "hello"
        self.__c = "hello"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

obj1 = Base()
print(obj1.a)

#destructor in python
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj