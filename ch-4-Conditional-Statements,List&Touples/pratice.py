
#! A program that takes a number as input and prints:- Positive if number > 0, negative if number < 0, and Zero if number  == 0.

number = int(input("Enter a number:"))

if(number > 0):
  print("Number is Positive")
elif(number < 0):
  print("Number is Negative")
else:
  print("Number is Zero")