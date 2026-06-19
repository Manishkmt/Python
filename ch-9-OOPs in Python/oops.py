
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
class student:
  def __init__(self, name):
    self.name = name

  def hello(self):
    print("Hello", self.name)

s1 = student("Manish Kumawat")
s1.hello()
