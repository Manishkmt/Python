
#! Function Parameters & Arguments:-
#?                                  Functions can accept paramenters, data passed from outside.
#? The values given when calling the function are arguments.

#* Example:-

def avarage(a,b):
  avg = (a + b)/2

  print(avg)

avarage(5,6)
avarage(7,7)


#! Functions with default arguments;-

def student(name = "Manish Kumawat"):
  print(name)

student()
student("Subash Kumawat")


#! Return Statement:-
#?                   The return statement is used to send  a value back from a function.
#? After return, the function stops execution.
#* Example:-

# def greet(name = "Manish"):
#   return name

# result = greet()
# print(result)

#! Defaut and Keyword Arguments:-

#? Default Aruments:-
#*                   If no argument is provided, a default value is used.
# Example:-
# def greet(name = "Manish Kuamwat"):
#   print("Hello", name)

# greet()
# greet("Subash Kumawat")


#? Keyword Arguments:-
#*                     We can use the parameter name while passing values.
# Example:-

def student_info(name, age):
  print(name, "is", age, " years old.")

student_info(age = 20, name = "Manish Kuamwat")


#! Variable Scope(Local vs Global):-

#? Local Variable:-
#*                  Defined inside a function-- accessible only within it.

#? Global Variable:-
#*                   Defined outside any function-- accessible everywhere.

# Example:-

x = 10  # global variable

def show():
  x = 5   # local variable
  print("Inside function:", x)

show()

print(x)



#! None in Python:-
#?                  None means no value.
#? If a function does not return anything, it automatically returns None.
# Example:-

def greet():
  print("Hello Manish")

result = greet()
greet(result)