# Functions :
#
# a block of code which is executes when it is called
#
# followed by def
#
#     def functioname(<parameters>)
#         code to be executed
# from builtins import function


# def hari():
#      print("Welcome to the chaos")
#
# hari()

# def doom():
#     print("hell answers to me")
#
# doom()

# arguments
#
# values to be passed to a functions
#
# parameters
#
# values mapped in the function

# types of argumennts

# 1. positional arguments

# def add(a, b):
#     print(a + b)
#
# add(10, 20)
#
# Here:
#
# 10 goes to a
# 20 goes to b
#
# The position matters.

# 2. keyword arguments

# def add(a, b):
#     print(a + b)
#
# add(b=20, a=10)

# Here, we use the parameter names a and b, so the order does not matter.

# return

# def add(a,b):
#     return a+b

# return sends a value from inside the function back to the place where the function was called.
# function will be terminated hereafter

# print(add(1,2)*10)

# If you mean f" in Python, it is used for an f-string.
#
# Generally
#
# f means: "I want to put variables directly inside this string."
#
# Example:
#
# name = "Harigesh"
#
# print(f"Hello {name}")
#
# print("Hello", name)

# Basic calculator with functions

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# while True:
#     print("Welcome to calculator")
#
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#
#     print("1. Add \n 2. Subtract,\n 3. Multiply \n 4. Divide")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         print(add(a, b))
#
#     elif choice == 2:
#         print(subtract(a, b))
#
#     elif choice == 3:
#         print(multiply(a, b))
#
#     elif choice == 4:
#         print(divide(a, b))
#
#     elif choice == 5:
#         break
#
#     else:
#         print("Invalid choice")

# 1. Age Calculator

# def age_calculator(born_year):
#     current_year = 2026
#     age = current_year - born_year
#     return age
#
# print("Welcome to age calculator")
# year = int(input("Please enter your born year: "))
#
# age = age_calculator(year)
#
# print("Your age is", age)

# 2.BMI calculator

# def bmi_calculator(weight, height):
#     bmi = weight / (height * height)
#     return bmi
#
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
#
# bmi = bmi_calculator(weight, height)
#
# print("Your BMI is", bmi)
#
# if bmi < 10.5:
#     print("You are underweight")
#
# elif bmi < 15:
#     print("You are normal weight")
#
# elif bmi < 20:
#     print("You are overweight")
#
# else:
#     print("You are obese")

# 3. Factorial
# def factorial(n):
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact = fact * i
#
#     return fact
#
#
# num = 5
# print(factorial(num))

