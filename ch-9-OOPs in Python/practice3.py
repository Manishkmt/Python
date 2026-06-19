
# ! Create class student that takes 3 marks and has a method avarage().

class student:
  
  def __init__(self, name, listOfMarks):
    self.name = name
    self.listOfMarks = listOfMarks
  def avarage(self):
    sum = 0
    for eachvalue in self.listOfMarks:
      sum = sum + eachvalue
    
    avarage = sum / 3
    print(avarage)
    

obj = student("Manish Kumawat", [100, 80, 90])

obj.avarage()