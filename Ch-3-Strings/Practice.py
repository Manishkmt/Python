
#!Program that takes your fav orite food name as input and print mid three ch and last two ch

str = input("Enter your favrorite food name:")

print(str)

length = len(str)

mid = length//2

print(str[mid-1:mid+2])

print(str[-3:-1])




