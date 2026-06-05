
#! Print how many lines are present in bio.txt

with open("ch-8-file handiling/bio.txt", "r") as f:
  listOfLines = f.readlines()

  print(listOfLines)

  print("Number of the lines :", len(listOfLines))