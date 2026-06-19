
# ! Create static method to validate if a number is even.

class number:

  @staticmethod
  def checknum(Num):
   num = Num
   if num % 2 == 0:
    print("num is even")
   else:
    print("num is odd")

obj = number()
obj.checknum(67)
  
