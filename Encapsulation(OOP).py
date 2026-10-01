# Encapsulation in Python OOP
#
# Encapsulation means wrapping data (variables) and methods (functions)
# together inside a class and controlling how the data can be accessed.
#
# In simple words:
#
# Encapsulation = Protecting data inside a class.

# Main purpose of encapsulation:
# Data hiding + controlled access to data.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# student1 = Student("Hari", 20)
#
# print(student1.name)
# student1.age = 25

# Here, name and age are inside the class, so this is encapsulation
# (data + methods grouped inside a class). But the data is freely accessible.

# In order to control the Access, we need to use the Access modifiers


# Access modifiers
#
# Access modifiers control how class attributes and methods are intended to be accessed.

# Unlike Java or C++, Python does not strictly enforce public, protected,
# and private; it mainly uses naming conventions and name mangling.
#
# Modifier	 Syntax	                Meaning
#
# Public	     self.name	            "Everyone can use it."
# Protected	     self._name	            "This is mainly for the class and child classes."
# Private	     self.__name	        "This is meant to stay inside the class."

# 1. Public — self.name
#
# Public means anyone can access it.
#
# class Student:
#     def __init__(self):
#         self.name = "Hari"   # Public
#
#
# student = Student()
#
# print(student.name)
#
# You can access name:
#
# Inside the class
# In a child class
# Outside the class
#
# So:
# Public = Everyone can use it.

# 2. Protected — self._name
#
# Protected uses one underscore _.
#
# class Student:
#     def __init__(self):
#         self._name = "Hari"   # Protected
#
#
# student = Student()
#
# print(student._name)
#
# Output:Hari
#
# Notice something important: Python still allows you to access _name from outside.
#
# The _ is mainly a warning/convention saying:
#
# This is intended for the class and its child classes.
# Don't access it directly unless you know what youre doing.

# So:
# Protected = Mainly for the class and child classes.

# 3. Private — self.__name
#
# Private uses two underscores __.
#
# class Student:
#     def __init__(self):
#         self.__name = "Hari"   # Private
#
#     def show(self):
#         print(self.__name)
#
#
# student = Student()
#
# student.show()
#
# Output: Hari
#
# But if you try:
#
# print(student.__name)
#
# you get an error because Python's name mangling changes the internal name.
#
# The important idea is:
#
# Private = Intended to be accessed only inside the class.
#
# SIMPLE:
#
# name       → Public     → Everyone
# _name      → Protected  → Class + Children
# __name     → Private    → Class only