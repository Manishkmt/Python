
#! Sets in Python:-
#?                 A Set is a collection of unordered and unique items. Seta automatically remove duplicate elements and are written using curly braces {}.

# Example:-
#           languages = {"Python", "Java", "C++", "Python"}
 # print(languages)

##* Output :- {"C++", "Java", "Python"}

# languages = {"Python", "Java", "C++", "Python"}
# print(type(languages))
# print(languages)

#! Creating a Set:-
#  empty_set = set()  # Empty set
# nums = {1, 2, 3, 4}  # Non-empty set

# empty = set()
# print(type(empty))


#! Set Properties:-

#? 1. Unordered--> no fixed index positions

#* 2. Unique--> no duplicates

#? 3. Mutable--> elements can be added or removed

#? 4. Cannot contain mutable elements like lists or dictionaries.

#! Adding and Removing Elements:-

nums = {1, 2, 3}
nums.add(4)
print(nums)

# nums.remove(3)
# print(nums)


#! Other useful methods:-

#? 1. .add(value):-
#                  Adds an Element
# Example:-
#          nums.add(4)
#          print(nums)


#? 2. .remove(value):-
#                      Removes Elements
# Example:-
          #  nums.add(4)
          #  print(nums)


#? 3. .clear():-
#                Empties the set.
# Example:-
# nums.clear()
# print(nums)

#? 4. .pop():-
#              Removes a rendom element.
# Example:-
nums.pop()
print(nums)


#? 5. .union(set2):-
#                   Combines two sets.
# Example:-
nums2 = {5, 6, 7, 8, 2}
update = nums.union(nums2)
print(update)


#? 6. .intersection(set2):-
#                           Common elements of boh sets.
# Example:-
inter = nums.intersection(nums2)
print(inter)



#! Difference between Dictionary & Set:-

#? 1. Dictionary stoes data as key-value pairs but Set store unique values only

#* 2. Dictionary Syntax:-
#                       {"key" : value}

#*     Set syntax:-
#                  {value1, value2, ...}

#? 3. Dictionary  and set both are mutable.

#* 4. In dictionary keys are unique,duplicasy not allow but in Set all elements are unique.

#? 5. In dictionary and set both are indexing not support.