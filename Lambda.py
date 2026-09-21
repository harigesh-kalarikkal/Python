# What is a lambda function?
#
# A lambda function is a small, one-line function in Python.
#
# It is mainly used when you need a simple function without writing the usual def function.
from idlelib.textview import view_text

# Basic pattern to remember
# variable = lambda inputs: calculation

# def square(x):
#     return x ** 2
#
# print(square(9))

# or

# square = lambda x: x ** 2
#
# print(square(9))
#
# Part	Meaning
# square	Name we give to the function
# =	Store the function in square
# lambda	Tells Python we are creating a lambda function
# x	Input/parameter
# :	Separates input from the calculation
# x ** 2	Calculation/returned result


# 1. Area of a circle
#
# Formula: π × r²

# area_circle = lambda r: 3.14 * r**2
#
# print(area_circle(8))

# 2. Area of a triangle
#
# Formula: 1/2 × base × height

# area_triangle = lambda b, h: 0.5 * b * h
#
# print(area_triangle(10, 5))

# 3. Square root of a number

# square_root = lambda n: n**0.5
#
# print(square_root(25))

# 4. Full name of a person
#
# We can join first name and last name:

# full_name = lambda first, last: first + " " + last
#
# print(full_name("Harigesh", "Kalarikkal"))

# 5. Average of 5 numbers
#
# Formula:
#
# (a + b + c + d + e) / 5

# average = lambda a, b, c, d, e: (a + b + c + d + e) / 5
#
# print(average(10, 20, 30, 40, 50))

# 6.Eligible to vote

# vote = lambda age: "Eligible to vote" if age >= 18 else "Not eligible to vote"
#
# print(vote(17))

# or

# age = 20
# print("eligible to vote") if age >= 18 else print("Not eligible to vote")