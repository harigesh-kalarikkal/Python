# A set is a collection of unique items.
#
# set is written using curly braces {}.

# numbers = {1, 2, 3, 4, 5}
#
# print(numbers)
#
# Properties of a Set:
#
# 1. Unique Values (No Duplicates)

# numbers = {1, 2, 2, 3, 3, 4}
#
# print(numbers)

# 2. Unordered

# fruits = {"apple", "banana", "orange"}
# villa = {10,2,3,7,5,9}

# print(fruits)
# print(villa)

# 3. Not Indexed

# fruits = {"apple", "banana", "orange"}
#
# print(fruits[0]) ❌ :'set' object is not subscriptable

# 4. Mutable

# numbers = {1, 2, 3}
#
# numbers.add(4)
# numbers.remove(2)
#
# print(numbers)

# 5. Mixed

# data = {"Harigesh", 25, 5.5, True}
#
# print(data)

# 6. Iterable

# fruits = {"apple", "banana", "orange"}
#
# for fruit in fruits:
#     print(fruit)

# 7.Nested? ❌ :Unlike lists, you generally cannot directly
# put a mutable set inside another set, because set elements must be immutable (hashable).