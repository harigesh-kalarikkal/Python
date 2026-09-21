# List questions

# 1.Print all elements in a list
# numbers = [10, 20, 30, 40, 50]
#
# for i in numbers:
#     print(i)

# 2.Find the sum of list elements
# numbers = [10, 20, 30, 40]
#
# sum = 0
#
# for i in numbers:
#     sum = sum + i
#
# print("Sum =", sum)
#
# 3.Find the largest element
# numbers = [10, 20, 30, 40]
#
# print("Largest =", max(numbers))
# print("largest =" , min(numbers))

# min() is a built-in Python function used to find the smallest value.
# max() is a built-in Python function used to find the largest value.



#
# 4.Count even numbers
# numbers = [1, 2, 3, 4, 5, 6]
#
# count = 0
#
# for i in numbers:
#     if i % 2 == 0:
#         count = count + 1
#
# print("Even numbers =", count)
#
# 5.Print list in reverse
# numbers = [10, 20, 30, 40, 50]
#
# print(numbers[::-1])

# Tuple questions:
#
# 1. Print tuple elements
# fruits = ("Apple", "Banana", "Orange")
#
# print(fruits)

# 2. Count total elements
# t = (10, 20, 30, 40, 50)
#
# print("Total elements =", len(t))
#
# len() is a built-in Python function used to
# find the number of elements in something.
#
# 3. Find maximum element
# t = (12, 45, 23, 67, 34)
#
# print("Maximum =", max(t))

# max() is a built-in Python function used to find the largest value.
#
# 4. Sum of tuple elements
# t = (5, 10, 15, 20)
#
# print("Sum =", sum(t))

# sum() is a built-in Python function used to add all the numbers together.

#
# 5. Search an element
# t = (10, 20, 30, 40)
# x = 20
#
# if x in t:
#     print("Element found")
# else:
#     print("Element not found")

# pass in Python is a placeholder statement when no codes need to executed
#
# Python requires something inside blocks like if, for, while, or functions.
# If you don't want to write the code yet, you can use pass.

# if 5 > 3:
#     pass

# This causes an error because the block is empty.

# enumerate() in Python
#
# enumerate() is a built-in function that gives both the
# index and the value while looping through a list, tuple, or other iterable.

# fruits = ["apple", "banana", "mango"]
#
# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# 1. Add Digits of a Number

# num = 12345
# sum = 0
#
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10
#
# print("Sum of digits =", sum)

# 2. Reverse of a Number

# num = 12345
# reverse = 0
#
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#
# print("Reverse =", reverse)

# 3.Fibonacci Series up to 100

# a = 0
# b = 1
#
# while a <= 100:
#     print(a)
#
#     c = a + b
#     a = b
#     b = c

# 4. Factorial of a Number

# num = 5
# factorial = 1
#
# while num > 0:
#     factorial = factorial * num
#     num = num - 1
#
# print("Factorial =", factorial)

# 5.Check Whether a Number is Prime or Not

# num = 7
# i = 2
# count = 0
#
# while i < num:
#     if num % i == 0:
#         count = count + 1
#
#     i = i + 1
#
# if count == 0 and num > 1:
#     print("Prime number")
# else:
#     print("Not a Prime number")


#6 You need to input a string and print every vowel along with its index.

# name = input("Enter a string: ")
#
# for i in range(len(name)):
#     if name[i] in "aeiouAEIOU":
#         print(name[i], "at index", i)

#7 remove duplicate from list

# numbers = [1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 6, 6, 6, 7, 7]
#
# original = []
#
# for i in numbers:
#     if i not in original:
#         original.append(i)
#
# print(original)

#8 Write a Python program to find the sum of all digits of a given number.
# a = 12345
# sum = 0
#
# while a > 0:
#     digit = a % 10
#     sum = sum + digit
#     a = a // 10
#
# print(sum)

#9 print largest and smallest number from this list

# a = [11, 230, 3, 5000, 6, -11, -2, 3, 999]
#
# largest = 0
# smallest = 0
#
# for i in a:
#     if i > largest:
#         largest = i
#
#     if i < smallest:
#         smallest = i
#
# print("Largest =", largest)
# print("Smallest =", smallest)
#
#10 Sort this in ascending order

# a = [11, 230, 3, 5000, 6, -11, -2, 3, 999]
#
# b = []
#
# for i in range(len(a)):
#     smallest = a[0]
#
#     for j in a:
#         if j < smallest:
#             smallest = j
#
#     b.append(smallest)
#     a.remove(smallest)
#
# print(b)

#11 Print both halves

# a = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# half = len(a) // 2
#
# b =[]
# c =[]
#
# for i in range(half):
#         b = b + [a[i]]
#
# for i in range(half, len(a)):
#         c = c + [a[i]]
#
# print("b =", b)
# print("c =", c)

#12 Print all the data one by one in a list

# data = "my name is python"
#
# a = data.split()
#
# print(a)
#
# # Or
#
# data = "hello my name is python"
# word = ''
# result = []
#
# for i in data:
#     if i != ' ':
#         word = word + i
#     else:
#         result.append(word)
#         word = ''
#
# result.append(word)
# print(result)

# 12 You are given three integers l, r, and k.
# Find how many numbers between l and r (including both l and r) are divisible by k.
# You only need to find the count, not print the numbers.

# l = 1
# r = 10
# k = 2
#
# count = 0
#
# for i in range(l, r + 1):
#     if i % k == 0:
#         count = count + 1
#
# print(count)

# data = '1 10 2 '
# newdata = data.strip()
# new = newdata.split()
# print(new)

# l = int(new[0])
# r = int(new[1])
# k = int(new[2])
#
# count = 0
#
# for i in range(l, r + 1):
#     if i % k == 0:
#         count = count + 1
#
# print(count)

# H
# for i in range(1, 6):
#     for j in range(1, 6):
#         if j == 1 or j == 5 or i == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# A
# for i in range(1, 6):
#     for j in range(1, 6):
#          if j == 1 or j == 5 or i == 1 or i == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# I
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# S
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 3 or i == 5 or (j == 1 and i == 2) or (j == 5 and i == 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(1, 6):
#         for j in range(1, 6):
#             if i == 1 or i == 3 or i == 5:
#                 print("*", end=" ")
#             elif i == 2 and j == 1:
#                 print("*", end=" ")
#             elif i == 4 and j == 5:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
