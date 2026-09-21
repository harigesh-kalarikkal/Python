# read
#
# file1= open("hari.txt","r") #r= read
# print(file1.read())
# file1.close()
import os

# overwrite

# file2= open("Doom.txt","w") # w= write
# file2.write("Hell answers to me")
# file2.close()

# add lines

# file3= open("Doom.txt","a") #a= append or add
# file3.write("\nI'm doom")
# file3.close()

# With function

# with open("Doom.txt","r") as file:
#     print(file.read())
#
# with open("Doom.txt","w") as file:
#     file.write("Hello World")
#
# with open("Doom.txt","a") as file:
#     file.write("\nHello Doom")

# import os
#
# os.mkdir("Alter")
# os.rename("Alter","Alter ego")
# os.remove("Alter ego")

# IMP = \\ consider as \

# path = "C:\\Users\\harig\\OneDrive\\Desktop\\EGO.txt"
#
# if os.path.exists(path):
#     if os.path.isdir(path):
#         print("Folder exists")
#     elif os.path.isfile(path):
#         print("File exists")

# 1. os.path.isdir()
#
# Checks whether the given path is a directory.
#
# 2. os.path.isfile()
#
# Checks whether the given path is a file.

# exceptional handling

# try:
#     a= 5
#     b= 3
#     print(a / b)
#
# except Exception as e:
#     print(e)

# try:
#     a= int(input("Enter a number: "))
#     b= 10
#     print(a/b)
#
# except ValueError:
#     print("Check your value")
# except TypeError:
#     print("Check your type")
# except ZeroDivisionError:
#     print("Division Error")
# finally:    #not must
#     print("This will be printed")


# Raise error

# class myerror(Exception):
#     pass
#
# age = 10
#
# if age >= 18:
#     raise myerror("Age should be less than 18")






