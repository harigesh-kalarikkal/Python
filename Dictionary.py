# Dictionary:collection that stores data in key : value pairs.
#
# Dictionary → {} > It uses curly brackets

# student = {
#     "name": "Harigesh",
#     "age": 25,
#     "course": "Python"
# }
#
# print(student.get("course"))
# print(student.get("name"))
# print(student.get("age"))

# Properties of a Dictionary:

# 1. Key-Value Pairs
# A dictionary stores data using:
#
# key : value

# student = {
#     "name": "Harigesh",
#     "age": 25
# }
#
# print(student.get("name"))

# 2.Mutable

# student = {"name": "Harigesh", "age": 25}
#
# student["age"] = 26
# student["name"] = "Batman"
#
# print(student)

# 3.Ordered

# student = {
#     "name": "Harigesh",
#     "age": 25
# }
# The items remain in the same insertion order.

# print(student)

# 4. Keys Must Be Unique ; You cannot have duplicate keys.

# student = {
#     "name": "Harigesh",
#     "name": "John"
# }
#
# print(student)
# The second "name" replaces the first one.

# 5. Values Can Be Duplicated
# data = {
#     "a": 10,
#     "b": 10,
#     "c": 20
# }
# print(data)
# Here, the value 10 appears twice.

# 6. Mixed
# student = {
#     "name": "Harigesh",
#     "age": 25,
#     "marks": 95.5,
#     "passed": True
# }
# # print(student)
#
# print(student.get("age"))

# 7. Nested

# student = {
#     "name": "Harigesh",
#     "details": {
#         "age": 25,
#         "course": "Python",
#         "college":  'Cooperative college'
#     }
# }
#
# print(student.get("details").get("college"))

# So, Dictionary → Key-based, not index-based.

