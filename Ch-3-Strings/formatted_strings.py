
#! Formatted Stringd(f-Strings) makes it easy to include variables inside strings.
#* Example:-
#           name = "Manish Kumawat"
#           age = 19
#           print(f"My name is {name} and i am {age} years old.")

name = "Manish Kumawat"
age = 19
print(f"My name is {name} and I am {age} years old.")


#! EScape Sequences:-
#*                   Escape sequences let you use formating in strings.

#? \n:-
#*     new line.
#* Example:-
#           "Hello\nWorld"--> print it in two lines
#? \t:- tab size
#* Example:- A\tB--> Adds a tab between A and B

#? \\:- Backlash
# Example:- "c:\\newfplder"-->c:\newfolder

#? \':- Single Quote
# Example:- 'It\'s gret--> It's  great

#? \" :- Double Quote
# Example:- "He said\"Hi\""--> He said "Hi"


print("Hello\nWorld")
print("Hello\tWorld")


#! Extra String operation:-
#? 1. Concatenation:-
#                 "Hello" + "Samosa" --> 'HelloSamosa'

#? 2. Repetition:-
#                 "Yum! " * 3 --> 'yum! Yum! Yum!

#? 3. Membership:-
#                 "a" in "banana"--> True
#                  "z" not in "mango"--> True

#? 4. len() Function:-
#                     len("Manish Kumawat")--> 11