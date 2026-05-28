
#!Conditional Statements:-
#?                        Conditional statements allow your program to make decisions - run different parts of code based on certain conditions.
# 
# --> A condition is simply a statement that can be either True or False.
# 
# Example:-
#          age = 19
# print(age >= 19) ## True


#! if Statement:-
#?               Used to run a block of code only when the condition is True.
#* Example 1:-

# age = int(input("Enter your age:"))

# if age >= 18: print("Your are eligible to vote.")

# else:
#  print("You are not eligble to vote")






#!--> If the condition is false, nothing happens.


#! if-else Statement:-
#?                    Used when we have multiple conditions.
  
marks = int(input("Enter your marks:"))
if(marks >= 90):
  print("the grade is A")

elif(marks >= 80):
  print("The grade is B")
elif(marks >= 70):
  print("The grade is C")
elif(marks >= 60):
  print("The grade is D")
else:
  print("You are fail")