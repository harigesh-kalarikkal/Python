# OOP stands for Object-Oriented Programming

# It is a programming method where we organize code using objects and classes.

# In simple words:
#
# OOP is a way of writing programs by creating classes and objects that contain data and functions.
#
# The main concepts of OOP are:
#
# Class
# Object
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# class Car:
#     def start():
#         print("Car can start")
#     def stop():
#         print("Car can stop")
#
# car1 = Car
# car2 = Car
# car2.start()
# car1.stop()

# class Bike:
#     def start():
#         print("Bike can start")
#     def stop():
#         print("Bike can stop")
#
# b1 = Bike
# b1.start()
# b2 = Bike
# b2.start()

# class Car:
#     def __init__(self, color, name, year):
#         self.color = color
#         self.name = name
#         self.year = year
#
#     def start(self):
#         print(f"{self.name} Car can start")
#
#     def stop(self):
#         print(f"{self.name} Car can stop")
#
# car1 = Car("red", "BENZ", 2000)
# car2 = Car("blue", "BMW", 2000)
# car1.start()
# car2.stop()

# Similar with Pen

# class Pen:
#     def __init__(self, name,color):
#         self.name = name
#         self.color = color
#
#     def use(self):
#             print(f"{self.name} can start writing")
#     def stop(self):
#             print(f"{self.name} can stop writing")
#
# pen1 = Pen("Lexi","blue")
# pen2 = Pen("Reynolds","red")
# pen1.use()
# pen2.stop()

# Create a class Student with 6 attributes: name, m1, m2, m3, m4, and m5.
# Create methods to calculate the sum of marks,
# calculate the average of marks, and display the student details.

# class Student:
#     def __init__(self, name, mark1, mark2, mark3, mark4, mark5):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#         self.mark4 = mark4
#         self.mark5 = mark5
#
#     def total_marks(self):
#         return self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
#
#     def average_marks(self):
#         return self.total_marks()/ 5
#
#     def display(self):
#         print("Name: " , self.name)
#         print("Sum of marks: " , self.total_marks())
#         print("Average marks: " , self.average_marks())
#
# student1 = Student("Alfred",50,60,70,80,90)
# student1.display()







