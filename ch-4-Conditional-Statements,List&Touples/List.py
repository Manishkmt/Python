
#! List in Python:-
#?                  A List is a built-in data type that can store multiple values in a single variable.
#*-->  Lists are mutable(can be changed) and can store different data types.

# Example:-

# marks = [67, 56, 68, 99, 59, 89, 100]

# foods = ["Samosa", "Burger", "Banana", " Apple"]

# pets = ["Dog", "Cow", "Cat", "Lion"]


# foods = ["Samosa", "Burger", "Banana", " Apple"]

# print(len(foods))

# print("First value of list is ", foods[0])

# print("second value of list is ", foods[1])

# print("fourth value of list is ", foods[3])

#! Modifing Elements:-
#?                    Lists are changable.

# Examples:-

# foods[0] = "Pineapple"
# print(foods)


#! List Slicing:-
#?               You can extract part of list using slicing.
# Examples:-
marks = [67, 56, 68, 99, 59, 89, 100]

# print(marks[1:4])
# print(marks[:6])
# print(marks[3:])


#! List Functions:-
#? 1. max():-
# print(max(marks))                

#? 2. min():-
# print(min(marks))  

#? 3. avg():-
# print(max(marks)) 

#? 4. .append():-
#                Adds element at the end.
# Example:-
          # marks.append(99) 

# marks.append(99)
# print(marks)

#? 5. .insert():-
#                Insert elements at index.
# Example:-
#          marks.insert(index num, value)

# marks.insert(2,88)
# print(marks)

#? 6. .remove():-
#               Remove first occurrence.
# Example:-
#           marks.remove(value)

# marks.remove(99)
# print(marks)

#? 7. .pop():-
#             Removes elements at index.
# Example:-
#             marks.pop(index num)

# marks.pop(6)
# print(marks)

#? 8. .sort():-
#              Sort list in ascending order
# Example:- 
#          marks.sort()

# marks.sort()
# print(marks)

#? 9. .reverse():-
#                  Reverse the list.
#Example:-
#          marks.reverse()

marks.reverse()
print(marks)

