
#! File Handling in Python:-
# ?                          File handling allows Python programs to store, read, and manage data saved on the computer - such as notes, logs, student records,or CSV files.

# ! Real world uses:-
# 1. Saving login page 
# 2. Writting Reports
# 3. Storing student Data 
# 4. Reading configuration files 
# 5. Exporting analytics in CSV 



# ! Types of files:-
# ? 1. Text files:-
#                   Human-readable content.
# Example:- .txt, .csv, .log

# ? 2. Binary files:-
#                     Data stored in encoded form
#  Example:- .png, .jpg, .mp4, .pdf, .exe


#! Opening files:-
# ?                Pythion uses the open() function to open a file.
# Example:-
#           file = open("fileName", "mode")


#! Some common modes:-
# ? "r" :- Read(default)

# * "w" :- Write(overwrites file)

# ? "a" :- Append(adds at end)

# * "x" :- Create new file; error if exixts

# ? "t" :- Text mode

# * "b" :- Binary mode

# ? read
# file = open("ch-8-file handiling/manish.txt", "r")
# data = file.read()
# print(data)

# ? wite
# file = open("ch-8-file handiling/manish.txt", "w")
# file.write("Manish")

# ? append

# file = open("ch-8-file handiling/manish.txt", "a")
# file.write("Welcome")


#! Reading files:-
# ? (a) Read entire file:-

# with keyword

# with open("ch-8-file handiling/manish.txt", "r") as f:
#   data = f.read()
#   print("file data", data)


#? (b) Read line by line:-

# with open("ch-8-file handiling/manish.txt", "r") as f:
#   data = f.readline()
#   print(data)

#? (c) Read all lines:-

with open("ch-8-file handiling/manish.txt", "r") as f:
  data = f.readlines()
  print(data)


# ! Automating File Tasks(copy, Rename, Delete):
# ?      using Python modules:-
# ?  Think of a module as a toolbox.
# ?  Each module gives you tools(functions) thst you don't have to write again.


# ! Copy file:-

# import shutill
# shutill.copy("demo.txt", "backup-demo.txt")


# ! Rename file:-
# import os
# os.rename("demo.txt", "new_demo.txt")

# ! Delete file:-
# import os
# os.remove("oldfile.txt")
 