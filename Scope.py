# What is Scope in Python?
#
# Scope in Python means the area of a program where a variable can be accessed or used.
#
# In simple words, scope tells us where a variable is available.
from asyncio import print_call_graph

# 1. Local Scope
#
# A variable created inside a function has local scope.
# It can be used only inside that function.
#
# def greet():
#     name = "Hari"
#     print(name)
#
# greet()
#
# Output:Hari
#
# Here, name is a local variable because it is created inside greet()

# 2. Global Scope
#
# A variable created outside a function has global scope.
# It can be accessed inside functions too.

# name = "Hari" #global
#
# def greet():
#     print(name) #local
#
# greet()
# print(name)

# Output:
#
# Hari
# Hari
#
# Here, name is a global variable.


# 3 Positional Arguments

# *args
#
# *args allows a function to accept multiple positional arguments.
#
# def numbers(*args):
#     print(args)
#
# numbers(10, 20, 30)
#
# Output:
#
# (10, 20, 30)
#
# args is a local variable inside the function.
#
# addz(1,2,3,4,5,5,5,6,7,7,7,7777)

# 4 Keyword arguments

# **kwargs
#
# **kwargs allows a function to accept multiple keyword arguments.

# def details(**kwargs):
#     print(kwargs)
#
# details(name="Hari", age=22)

# Output:
#
# {'name': 'Hari', 'age': 22}
#
# Here, kwargs is a local variable containing a dictionary.

# 5. Both
#
# *args + **kwargs Together
#
# You can use both:
#
# def student(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student("Python", "Linux", name="Hari", age=22)
#
# Output:
#
# ('Python', 'Linux')
# {'name': 'Hari', 'age': 22}

