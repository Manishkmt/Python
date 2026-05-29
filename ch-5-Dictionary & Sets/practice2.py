
#! You have given a list of programming langiages: ["Python", "Java", "C++", "Python", "Java", "C"].  Convert it into a set and print how many unique languages Divya knows.

languages = ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(languages))

setLanguages = {"Python", "Java", "C++", "Python", "Java", "C"}
print(type(setLanguages))


print(" Divya knows the",len(setLanguages),"languages: ",setLanguages)


