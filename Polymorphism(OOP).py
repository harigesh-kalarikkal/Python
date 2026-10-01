# What is Polymorphism?
#
# Polymorphism means:
#
# One thing can have many forms.
#
# In Python, polymorphism allows the same method or function name to behave differently depending on the object.
#
# Simple real-life example
#
# Think about the word "sound":
#
# Dog → bark
# Cat → meow
# Cow → moo
#
# They all have a sound() method, but each one behaves differently.

# class Dog:
#     def sound(self):
#         print("Dog barks")
#
#
# class Cat:
#     def sound(self):
#         print("Cat meows")
#
#
# dog = Dog()
# cat = Cat()
#
# dog.sound()
# cat.sound()
#
# Output:
#
# Dog barks
# Cat meows
#
# Here, both classes have the same method name: sound()
#
# But the method behaves differently for each object.
#
# That's polymorphism.
#
#
# What is Operator Overloading?
#
# Operator overloading means giving a special meaning to an operator such as:
# +   -   *   /   ==
#
# depending on the objects being used.


# 1.Addition

# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, otr):
#         t1 = self.m1 + self.m2
#         t2 = otr.m1 + otr.m2
#
#         return t1, t2
#
#
# s1 = Student(8, 10)
# s2 = Student(7, 9)
#
# print(s1 + s2)

# 2.Subtraction

# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __sub__(self, otr):
#         t1 = self.m1 - self.m2
#         t2 = otr.m1 - otr.m2
#
#         return t1, t2
#
#
# s1 = Student(8, 10)
# s2 = Student(7, 9)
#
# print(s1 - s2)

# 3. Multiplication

# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __mul__(self, otr):
#         t1 = self.m1 * self.m2
#         t2 = otr.m1 * otr.m2
#
#         return t1, t2
#
#
# s1 = Student(8, 10)
# s2 = Student(7, 9)
#
# print(s1 * s2)

# 4. Division

# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __truediv__(self, otr):
#         t1 = self.m1 / self.m2
#         t2 = otr.m1 / otr.m2
#
#         return t1, t2
#
#
# s1 = Student(8, 10)
# s2 = Student(7, 9)
#
# print(s1 / s2)


# 1. Method Overloading
#
# Method overloading means having the same method name but different parameters.
#
# class Calculator:
#
#     def add(self, a=0, b=0):
#         return a + b
#
#
# c = Calculator()
#
# print(c.add(5, 10))
# print(c.add(5))
# print(c.add())
#
# Here, the same add() method can work with different numbers of arguments.
#
# Simple meaning:
#
# Overloading = Same method, different inputs.

# 2. Method Overriding
#
# Method overriding happens when a child class provides
# its own version of a method that already exists in the parent class.
#
#     class Animal:
#
#         def sound(self):
#             print("Animal makes a sound")
#
#     class Dog(Animal):
#
#         def sound(self):
#             print("Dog barks")
#
#     animal = Animal()
#     dog = Dog()
#
#     animal.sound()
#     dog.sound()
#
# The Dog class overrides the sound() method of the Animal class.
#
# Simple meaning:
#
# Overriding = Child class changes the parent's method.

# Easy way to remember
#
# Overloading:
# One class → same method → different arguments
#
# Overriding:
# Parent class → Child class → same method → new behavior