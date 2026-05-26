
#!Datatypes in Python
#* Python has several built-in datatypes. They define the type of value of variable.
#?int: whole numbers are positive or negative.

#?float: Numbers with decimanls.

#?str: Sequence of characters.

#?bool: logical values--> true or false.


# name = "Manish"
# age = 19
# area = 32.2

# print("Datatype of name:",type(name))
# print("Datatype of age:",type(age))
# print("Datatype of area:",type(area))


#!program to take age as input and print value entered and its datatype

# age = input("Enter the age:")
# print("Age is",age)
# print("Datatype of age is",type(age))


#!Keywords
#?--> Keywords are the reserved words that have special meaning in pyhon and cannot be used as variable names.

#?Examples:
            # 1.and   2.as   3.assert   4.break   5.class
            #? 6.continue    7.def   8.elif    9.del   10.else
            # 11.except   12.False    13.finally    14.for    15.from
            #? 16.global   17.if   18.import   19.in   20.is
            # 21.lambda   22.None    23.noniocal    24.not    25.or
            #? 26.pass   27.raise    28.return   29.True   30.try
            # 31.while    32.with   33.yield

            #!Use help("keywords") in python shell to list all current keywords.


#!Syntax:-
            #?Syntax refers to the set of rules that defines how a python program is structured and written so thst the python intrepreter can understand and execute it correctly


# name = "manish"



#! Input two num and sum
# input1 = int(input("Enter first num:"))
# input2 = int(input("Enter second num:"))

# sum = input1 + input2

# print(sum)


#!Type Conversion:-

#?--> convert the datatype from one to another


#!Types:-
#?-->1.Implicit--> automatically Coberts the small datatype to larger to prevent data loss.

# x = 5
# y = 5.5
# z = x + y
# print(type(x))
 #*2.Explicit-->Manually converts datatypes using built in function.
  #  x = "10"
  #  y = int(x)


#!Operators in python
#?--> Operators perform operations on variables and values.
#?example:Airthmetic,comparsion, logical

x = 5
y = 7
print(x==y)
print(x<y)
print(x>y)

print(x>y and x<y )

x = 5
y = 7


print(x>y or x<y )

print(not (x<y) )
