
#!String in Python
#?-->A string is a datatype in Python that stores a sequence of characters - letters, numbers, or symbols - enclosed in single(''), double(""), or triple(''' ''') quotes.
# Examples-->
# str1 = 'Hello'
# str2 = "Manish Kumawat"
# str3 = '''Welcome in Python'''

#!Note:-
     #*--> Strings are immutable(values can't change), meaning once created, their content cannot be changed directly.


str1 = 'Hello'
str2 = "Manish Kumawat"
str3 = '''Welcome in Python'''

# print(str1)
# print(str2)
# print(str3)

#! String Concantenation
    #*--> If we add two string together then it called as String Concantention
#?print("Hello "+"World") ## Output--> Hello World

# print(str1 +" "+ str2)

#! LEngth of String
  #*--> We use this for the calculate the length of string
#?--> len("Mango")  ## Output--> 5

# print(len(str1 + str2))


#! Indexing
  #?--> Each character in a string has a position(index) starting from 0.

  # Example:-
  #       str2 = "Manish Kumawst"

length = len(str2)
print(str2[0])

print(str2[6])

print(str2[7])
