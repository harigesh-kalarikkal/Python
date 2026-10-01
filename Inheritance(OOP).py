# Inheritance

# Inheritance means creating a new class from an existing class.
#
# The new class can use the variables and methods of the existing class.
#
# Parent class → existing class
# Child class → new class that inherits from parent

# SINGLE INHERITANCE from 1 to 2
# class Person1:   #Parent class
#
#     def __init__(self):
#         pass
#
#     def jump(self):
#         print("person1 can jump")
#
#     def walk(self):
#         print("person1 can walk")
#
# class Person2(Person1):   #child class
#     def __init__(self):
#         pass
#
#     def run(self):
#         print("person2 can run")
#
#     def drive(self):
#         print("person2 can drive")
#
#     def drink(self):
#         print("person2 can drink")
#
# # p2=Person2()
# # p2.jump()
# # p2.walk()
#
# # MULTIPLE INHERITANCE = Person1 to 4
# class Person3(Person2):   #child class
#
#     def __init__(self):
#         pass
#
#     def fly(self):
#         print("person3 can fly")
#
#     def eat(self):
#         print("person3 can eat")
#
# class Person4(Person3):     #child class
#
#     def __init__(self):
#         pass
#
#     def cook(self):
#         print("person4 can cook")
#
#     def eat(self):
#         print("person4 can eat")
#
#     def drink(self):
#         print("person4 can drink")
#
#         #or
#
# class Person4(Person2):     #child class
#
#     def __init__(self):
#         pass
#
#     def cook(self):
#         print("person4 can cook")                   #Seperate code to know about super()
#
#     def eat(self):
#         print("person4 can eat")
#
#     def drink(self):
#         print("person4 can drink")
#         super().drink()   # So super() means go to the parent class (Person2) and it can use anywhere,
                            # if you would like to make it your parent class


# p4 = Person4()
# p4.cook()
# p4.eat()
# p4.run()
# p4.walk()
# p4.drink()

# Levels / Types of Inheritance
#
# There are 5 common types of inheritance in Python:
#
# 1.Single Inheritance
# 2.Multiple Inheritance
# 3.Multilevel Inheritance
# 4.Hierarchical Inheritance
# 5.Hybrid Inheritance

# 1. Single Inheritance
#
# One parent → One child
#
# Animal
#    ↓
#   Dog
# class Animal:
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#
#
# d = Dog()
# d.eat()
# d.bark()

# The Dog class inherits from only one parent

# 2. Multiple Inheritance
#
# Multiple parents → One child
#
# Father ──┐
#          ↓
#        Child
#          ↑
# Mother ──┘
#
# class Father:
#     def skill1(self):
#         print("Driving")
#
#
# class Mother:
#     def skill2(self):
#         print("Cooking")
#
#
# class Child(Father, Mother):
#     pass
#
#
# c = Child()
#
# c.skill1()
# c.skill2()
#
# Here Child inherits from both Father and Mother.

# 3. Multilevel Inheritance
#
# Grandparent → Parent → Child
#
# Animal
#    ↓
#  Mammal
#    ↓
#   Dog

# class Animal:
#     def eat(self):
#         print("Eating")
#
#
# class Mammal(Animal):
#     def walk(self):
#         print("Walking")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("Barking")
#
#
# d = Dog()
#
# d.eat()
# d.walk()
# d.bark()
#
# Dog can access methods from both Mammal and Animal.
#
# This is called multilevel inheritance because inheritance happens through multiple levels.

# 4. Hierarchical Inheritance
#
# One parent → Multiple children
#
#        Animal
#        /    \
#       ↓      ↓
#     Dog     Cat
#
# class Animal:
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#
#
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
#
#
# d = Dog()
# c = Cat()
#
# d.eat()
# d.bark()
#
# c.eat()
# c.meow()
#
# Both Dog and Cat inherit from Animal.

# 5. Hybrid Inheritance
#
# Combination of two or more types of inheritance.
#
# For example:
#
#        Animal
#        /    \
#       Dog    Cat
#        \     /
#         \   /
#         Pet
#
# It combines different inheritance structures.
#
# class Animal:
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#
#
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
#
#
# class Pet(Dog, Cat):
#     pass
#
#
# p = Pet()
#
# p.eat()
# p.bark()
# p.meow()
#
# Here different inheritance types are combined, so it is called hybrid inheritance.

# 1. Method Overriding
#
# Method overriding means a child class provides
# its own version of a method that already exists in the parent class.
#
# In simple words:
#
# Same method name, but the child changes what the method does.
#
# Example
#
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
#
# d = Dog()
# d.sound()
# Output >>> Dog barks

# 2. super()
#
# super() is used to call a method or constructor from the parent class.
#
# Example
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
#
#
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")
#
#
# d = Dog()
# d.sound()
#
# Output :
# Animal makes a sound
# Dog barks

# Call the sound() method from the parent class.

# 3.METHOD RESOLUTION ORDER

# MRO means Method Resolution Order.
#
# Method Resolution Order (MRO) is the order in which Python searches the classes
# to find a method or attribute when using inheritance.

# class A:
#     def show(self):
#         print("A")
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass
#
# c = C()
# c.show()
#
# Output: A
#
# Python searches in this order: C → B → A
#
# It doesn't find show() in C or B, so it finds it in A.
#
# In short: MRO tells Python where to look for a method first, second, third, etc.

# MRO tells Python where and in what order to look for a method in an inheritance hierarchy.

# Q) Plot the points on a Cartesian plane which has 2 coordinates x and y. Do the following:
#
# 1. Define a class Point. Its instance should have 2 attributes x and y.
# x and y default value must be zero.

# class Point:

# 1. Define a class Point. Its instance should have 2 attributes x and y.
# x and y default value must be zero.

    # def __init__(self, x=0, y=0):
    #     self.x = x
    #     self.y = y


# 2. Define an instance method reset(). When called, it will set x, y values to zero
# (i.e., it will set the point to origin (0,0)).


# 3. Define a method move(). This should change the values of x and y.

    # def move(self, x, y):
    #     self.x = x
    #     self.y = y


# 4. Use this move() method to update the reset() method.

    # def reset(self):
    #     self.move(0, 0)


# 5. Define 2 methods xmove() and ymove().
# This should move the values of x and y separately.

#     def xmove(self, x):
#         self.x = x
#
#     def ymove(self, y):
#         self.y = y
#
# p = Point()
#
# print(p.x, p.y)
#
# p.move(5, 10)
# print(p.x, p.y)
#
# p.xmove(20)
# print(p.x, p.y)
#
# p.ymove(30)
# print(p.x, p.y)
#
# p.reset()
# print(p.x, p.y)

# Q). Write a Python class Queue that implements a basic queue data structure
# with the enqueue and dequeue methods.
#
# The enqueue method should add an element to the rear of the queue,
# and the dequeue method should remove and return the remaining element from the queue.
#
# Additionally, include a method is_empty to check if the queue is empty.


# class Queue:

    # Create an empty queue
    # def __init__(self):
    #     self.queue = []


    # Enqueue: Add an element to the rear of the queue

    # def enqueue(self, element):
    #     self.queue.append(element)


    # Dequeue: Remove and return an element from the queue

    # def dequeue(self):
    #     if self.is_empty():
    #         return "Queue is empty"
    #     return self.queue.pop(0)


    # is_empty: Check if the queue is empty

    # def is_empty(self):
    #     return len(self.queue) == 0


# Create object
# q = Queue()
#
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
#
# print(q.queue)
#
# print(q.dequeue())
# print(q.dequeue())
#
# print(q.queue)
#
# print(q.is_empty())