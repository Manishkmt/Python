
#! Wap to print numbers from 1 to 50, but print "Manish Kumawat" instead of numbers that are multiple of 5.
#? Example;- 1 2 3 4 Manish Kumawat 6 7 8 9 Manish Kumawat.....

for item in range(1, 51,1):
  if(item % 5 == 0):
    print("Manish Kumawt")
  else:
    print(item)