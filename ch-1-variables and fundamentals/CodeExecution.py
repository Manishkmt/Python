# name = "Manish Kumawat"
# age = 19

# print(name)

# print(id(name))

# print("Actual Value:",age)


#?Taking user input
#*--> Use input90 to get user input

#*--> Example:
#*         name = input('Enter your name: ')
#*         print('Hello', name)
#!input() alwaye returns string
# 
#*-->Convert it before performing calculations    

# name = input("Enter your name:") 


# age = input("Enter your age:")
# print(name) 
# print(age)


#! Indentation
#*--> Indentation in python is meaningful. You cannot indent randomly like this:
#*       name = "Manish"
#*       print(name)


#?!Take diameter as input and claculate the area of a circle
import math

# Input diameter
diameter = float(input("Enter diameter: "))

# Calculate radius
radius = diameter / 2

# Calculate area
area = math.pi * radius * radius

# Output
print("Area of circle =", area)