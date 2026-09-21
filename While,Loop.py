# H=0
# while H<=100:
#     print(H)
#     H=H+10

# task

# print first 10 even numbers
# i = 2
# count = 1
#
# while count <= 10:
#     print(i)
#     i = i + 2
#     count = count + 1

#
# print first 10 odd numbers

# i = 1
# count = 1
#
# while count <= 10:
#     print(i)
#     i = i + 2
#     count = count + 1
#
# print the multiplication table of 5

# i = 1
#
# while i <= 10:
#     print(5, "x", i, "=", 5 * i)
#     i = i + 1

# Task
#
# reverse the number = 123

# num = 123
# reverse = 0
#
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#
# print(reverse)

# calculator
# menu driven
# add, sub, mul, div
# add 2,3=5
# sub 5,2=3

# while True:
#     print("Calculator")
#     print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5.Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#
#     if choice == 1:
#         print("Addition =", a + b)
#         break
#
#     elif choice == 2:
#         print("Subtraction =", a - b)
#         break
#
#     elif choice == 3:
#         print("Multiplication =", a * b)
#         break
#
#     elif choice == 4:
#         print("Division =", a / b)
#         break
#
#     else:
#         print("Please enter a valid choice")

for i in range(1, 6):
        if i == 3:
            break
        print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)




