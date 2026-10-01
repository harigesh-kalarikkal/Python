# Abstraction in Python OOP

#Abstraction means hiding unnecessary internal details and showing only what the user needs.

# Real-life example:
#
# Think about a car.
#
# When you drive a car, you use:
#
# start()
# accelerate()
# brake()
#
# You don't need to know exactly how the engine internally works.
#
# That is abstraction — you use the functionality without worrying about the internal implementation.
#
#Example
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def makes_sound(self):
#         pass
#
#
# class Dog(Animal):
#
#     def makes_sound(self):
#         print("woff woff")
#
#
# d = Dog()
# d.makes_sound()
#
# abc → Python's built-in module for Abstract Base Classes
# ABC → class used to create an abstract class
# abstractmethod → decorator that makes a method compulsory for child classes


