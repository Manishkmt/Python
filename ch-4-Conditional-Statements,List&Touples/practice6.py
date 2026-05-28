
#! Program to check grade based on marks (A/B/C/D) using if-elif-else

marks = int((input("Enter your marks: ")))
print(marks)

if(marks >= 90):
  print("the grade is A")

elif(marks >= 80):
  print("The grade is B")
elif(marks >= 65):
  print("The grade is C")
elif(marks >= 50):
  print("The grade is D")
else:
  print("You are fail")