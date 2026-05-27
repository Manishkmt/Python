
str = "Manish kumawat"

 #! Common String Methods:-
#?upper:-
#*      Converts all characters to uppercase
#* Example:-
#           "samosa".upper()-->'SAMOSA'

print(str.upper())

#? lower():-
#*          Converts all characters to lowercase.
#* Example:-
#           "Manish".lower()-->'manish'
print(str.lower())

#? title():-
#*          Capitalize the first letter of each word.
#* Example:-
#           "hello world".title()-->'Hello World'
print(str.title())

#? find(sub):-
#*            Returns index of first occurrence.
#* Example:-
#           "banana".find("na")-->2

print(str.find("an"))

#? replace():-
#*            Replace old character with new

print(str.replace("Manish","Subash"))

#? count():-
#*          Count the given character or find the occarance.
print(str.count("a"))