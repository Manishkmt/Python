
#! Write a code to open a file named mydata.txt in read mode

file = open("ch-8-file handiling/mydata.txt", "r")

data = file.read()

print("The data of user is:")
print(data)

file.close()