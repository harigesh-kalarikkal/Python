# List comprehension is a short and simple way to create a list using a for loop.

# b = [i for i in range(1, 101)]
# print(b)

#1. range(1, 101)

# This generates numbers from 1 to 100.

# 2. for i in range(1, 101)
# So i becomes:
#
# 1
# 2
# 3
# ...
# 100

# 3. [i ...]
# The i before for tells Python what to put into the list.
#
# So:
# [i for i in range(1, 101)]

# means:
# "Take every i from 1 to 100 and put it into a list."

# numbers = [i for i in range(1, 6)]
#
# print(numbers)
#
# c = [i for i in range(1, 1001) if i % 2 == 0]
# print(c)

# We can also perform calculations
#
# For example, create squares:
#
# squares = [i * i for i in range(1, 6)]
#
# print(squares)
#
# 1. Create a list of squares of numbers from the first 100 numbers
#
# squares = [i * i for i in range(1, 101)]
#
# print(squares)
#
# 2. From a list of 100 numbers, create a list of numbers divisible by 5 and 3
#
# numbers = [i for i in range(1, 101)]
#
# result = [i for i in numbers if i % 5 == 0 and i % 3 == 0]
#
# print(result)
#
# 3. Create a list of numbers that have the digit 6 in them from a range of 1000 numbers
#
# numbers = [i for i in range(1, 1001) if "6" in str(i)]
#
# print(numbers)

# Easy pattern to remember:
# [what_you_want for i in range(...) if condition]

