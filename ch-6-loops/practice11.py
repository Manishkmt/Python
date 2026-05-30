
#! Wap that prints the multiplication table of any number entered by the user using for loop.

num = int(input("Enter a number:"))
for item in range(1, 11, 1):
  print(num, "*", item,"=", num * item)