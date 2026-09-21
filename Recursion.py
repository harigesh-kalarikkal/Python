

# What is Recursion?
#
# Recursion is when a function calls itself.
#
# In simple words:
#
# A function repeatedly calls itself to solve a smaller version of the same problem.
#
# Recursion = A function calling itself until a stopping condition is reached.

# def hello():
#     print("hey hari")
#     return hello()
#
# hello()

# A recursive function always has two parts:
#
# Base case – the condition that stops the recursion.
# Recursive case – where the function calls itself with a smaller or simpler input.

# def factorial(n):
#     if n == 1:          # Base case
    #     return 1
    # else:
    #     return n * factorial(n - 1)  # Recursive case

# print(factorial(5))

# def count(n):
#     print(n)
#     if n == 0:
#         return
#     return count(n-1)
#
# count(5)

# The condition is true, so return executes.
#
# The function stops.

# Sum of numbers

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n - 1)
#
# print(sum(10))

# sum(10)
# = 10 + sum(9)
# = 10 + 9 + sum(8)
# = 10 + 9 + 8 + sum(7)
# ...
# = 10 + 9 + 8 + ... + 1 + sum(0)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# How this works :

# 5 × factorial(4)
#
# 5 × 4 × factorial(3)
#
# 5 × 4 × 3 × factorial(2)
#
# 5 × 4 × 3 × 2 × factorial(1)
#
# 5 × 4 × 3 × 2 × 1 × factorial(0)

num = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()