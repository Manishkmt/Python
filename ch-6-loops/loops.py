
#! loops in Python:-
#                    In Python, loops are used to repeat a block of code multiple times.

#* They help perform tasks like printing a message several times, iterating over lists, or generating patterns.

# Example:-
#          print("Manish Kumawat")
          #  print("Manish Kumawat")
          #  print("Manish Kumawat")
          #  print("Manish Kumawat")

# Instead of writing this three times, we can use a loop.


#! Types of loops:-

#? 1. while loop:-
#                 A while loop runs as long as acondition is true.

# Syntax:-
# while condition:
#   code block

# num = 1;

# while num <= 5:
#   print("Manish Kumawat")
#   num = num + 1

#? 2. for loop:-
#               A for loop is used to iterate (go through) sequences like lists, touples or strings.

#* Syntax:-
#           for element in sequence:
#           code block

# Example:-

# foodslist = ["Samosa", "GulabJuman", "Rasgulla"]
# for item in foodslist:
#   print("Manish likes", item)


# subjectstouple = ("C", "C++", "Java", "Python")
# for item in subjectstouple:
#   print(item)


#!for loop with range():-
#?                        The range() function generates a sequence of numbers. It is often used with loops.

#* Syntax:-
#           range(start, stop, step)
# 
#? start--> beginning number (default = 0)
# ? stop--> end limit (executed)
# ? step--> increment value (default = 1)   
# 
# Example:-

# for i in range(1, 6):
#   print("Iteration:", i)    

# for item in range(2, 20, 2):
#   print(item)   


#! Break, continue, and pass:-

#? 1. break statement:-
#*                      The break statement stops the loop immediately when it is encountered.
# Example:-
# for num in range(1, 10):
#   if num == 5:
#     break
#   print(num)

#? 2. continue statement:-
#*                        THe continue statement Skips the current iteration and proceeds to the next iteration.
# Example:-

# for num in range(1, 10):
#   if num == 5:
#     continue
#   print(num)

#? 3. pass statement:-
#*                    pass statement is used as a placeholder when you don't want to write code yet.
# Example:-

for num in range(1, 10):
  pass
