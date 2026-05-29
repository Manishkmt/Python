
#! Dictionary in Python:-
#?                       A Dictionary is built-in datatype in python used to store data in key-value pairs.
# Each key is unique and map to a value.

#! Dictionary are unordered, mutable(Changable), and don'gt allow duplicate keys.

# Example:-
#          student = {
#                "name" : "Manish       Kumawat",
# "age" : 19,
# "city" : "Kuchaman"
# }  

# Here "name", "age", "city"--> keys
#       "Manish Kumawat", 19, "Kuchaman"--> values


#! Accessing Values:-
#?                    you can access a value using its key:
student = {
 "name" : "Manish Kumawat",
"age" : 19,
"city" : "Kuchaman"
} 

# print(type(student))

# print(student["name"])
# print(student["age"])
# print(student["city"])

# print(student)

#? Replace values:-

# student["city"] = "Jaipur"
# print(student)

#? Add new Keys:-

# student["favSubject"] = "Python"
# print(student)


#? Remove keys or items:-
# student.pop("favSubject")
# print(student)

#! Dictionary method:-
#? 1. .key():-
#             Returns all keys
#Example:-student.keys()


print(student.keys())

#? 2. .values():-
#                Return all values
# Example:- student.values()

print(student.values())


#? 3. .items:-
#              Returns all key-value pairs as tuples.
# Example:- student.items()

print(student.items())

#? 4. .get(key):-
#                 Returns value of a key safely.
# Example:- student.get("name")

print(student.get("name"))
print(student.get("age"))


#? 5. .update(new_dict):-
#                        Update dictionary with another.
# Example:-student.update({"new_dict" : "value"})

print(student.update({"favSubject" : "Python"}))

