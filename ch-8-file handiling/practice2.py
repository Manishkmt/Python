
# ! Writ a program to read a text from a given file certificate.txt and find whether it contins the word live.
import os

print("Current Folder:", os.getcwd())

file = open(r"C:\Users\manish\OneDrive\Desktop\Python\ch-8-file handiling\certificate.txt", "r")
dataOfFile = file.read()
print(dataOfFile.lower())

if "live" in dataOfFile:
  print("Yes word is present in the file")
else:
  print("No")