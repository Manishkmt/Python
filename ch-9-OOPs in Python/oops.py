
# ! OOPS in Python:-
# ?                 OOp is a programming style where we use :

# class --> A class is a blueprint or template used to create objects. It defines the properties (variables) and behaviors (methods) that objects will have.

#  object --> An object is an instance of a class. It is a real entity that contains data (attributes) and functions (methods) defined in the class.

#  Attributes --> Attributes are variables that belong to a class or an object. They store the data or properties of an object.

# Methods -->


# ! Use of OOP:-
# 
# ? It makes code:-
# usable
# organized
# Easy to maintain
# Similar to real-world objects


# ? class creation:-

# class vehicle:
#   # Attributes
#   color = "Black"
#   milage = 15
#   cost = 5000000

# object creation
# car = vehicle()
# print(car.color)


# ? Instance Attributes vs class Attributes:-

# * Class Attributes shared by all objects

# class student:
#   college = "xyz"

# * Instance Attributes is unique for each object.

# class student:
#   college = "xyz"


  # ! __init__() Constructor:-
# ?                            The __init__() function runs automatically whenever an object is created. It used to initialize attributes.
# class student:
#   name = "Manish Kumawat"

#   def __init__(self,name1):
#     print("whenever a object is created then init constructor called automatically")
#     self.name1 = name1
    

# student1 = student("Subash Kumawat") # init method called
# print(student1.name1)
# print(student1.name,"\n")
# student2 = student("Khusharth Sharma") # init method called

# print(student2.name1)


# ! Methods (functions inside class):-
# ?                                   Methods define what an object can do.

# Example:-
# class student:
#   def __init__(self, name):
#     self.name = name

#   def hello(self):
#     print("Hello", self.name)

# s1 = student("Manish Kumawat")
# s1.hello()


# ! Ststic methods:-
# ?                  Static methods do not use self. They are used for utility-level functions.

# Example:-
# class student:
#   @staticmethod
#   def name():
#     print("Manish Kumawat")

# obj = student()
# obj.name()


# ! OOPS Concepts:-

# ? Abstraction:-
# *              Showing only essential details, hiding internal complexity.

# Example:- you use instagram without knowing its backend code.

# class payment:
#   @staticmethod
#   def pay():
#     print("Payment successful")

# obj = payment
# obj.pay() 

# ? Encapsulation:-
# *                 Wrapping data + methods inside a single unit (class). Data is protected using private variables.

# Example:-

# class account:
#   def __init__(self, bal):
#    self.balance = bal # Private

#   def show_balance(self):
#     print("Balance:", self.balance)

# obj = account(18900)
# obj.show_balance()


# ? Inheritance:-
# *               When one class (child) gets the properties and methods of another class (parent). It avoid repeating code.

#  Example:-  Child class uses everything the parent class already has.

# parent class 
# class vehicle:
#   def start(self):
#     print("Vehicle is starting")

# # child class

# class car(vehicle):
#   def drive(self):
#     print("car is moving now")

# # child class 2

# class bike(vehicle):
#   def ride(self):
#     print("bike is now riding")

# # using the class
# c = car()
# c.start() # from parent

# c.drive() # child specific

# b = bike()

# b.start() # from parent

# b.ride() # child specific


# ? Polymorphism:-
# *                Same function name, but different behaviour in different classes.

# * One function name --> many differnet behaviours depending on the object calling it.

#  Example:- Different objects respond in their own unique way.

class dog:
  def sound(self):
    print("Dog says : bark")

class cat:
  def sound(self):
    print("cat says: meow")

class cow:
  def sound(self):
    print("cow says : moo")

#  Polymorphism in action

animals = [dog(), cat(), cow()]

for a in animals:
  a.sound()