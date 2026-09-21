# What is a nested loop?
#
# A nested loop means:A loop inside another loop.
#
# Think of it like a box inside another box.

for i in range(1, 4):        # Outer loop
    for j in range(1, 4):    # Inner loop
        print(i, j)

# i → outer loop
# j → inner loop
# The j loop is inside the i loop.
# Therefore, this is a nested loop.

# the ending number in range() is not included.
#
# Python's range(start, stop) works as:
#
# Start at start and stop BEFORE stop.
#
# So the last number is always one less than the number inside range().

# For each one value of the outer loop, the inner loop runs completely.
#
# It is commonly used for patterns, tables, matrices, comparing items,
# and working with rows and columns.

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "mango"]
#
# for i in adj:
#     for j in fruits:
#         print(i, j)


