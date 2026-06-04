
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

file = open("ch-8-file handiling/manish.txt", "r")
data = file.read()
print(data)
 