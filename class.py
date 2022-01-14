class Person:
  def __init__(self, name, age): 
   self.name = name
   self.age = age
  def myfunc(self): 
    print("Hello my name is " + self.name)

p1 = Person("John", 36) 
print(p1.name) 
print(p1.age)
p1.myfunc()

#sistemare qui
class Element:
  def __init__(self, name, symbol, num): 
   self.name = name
   self.symbol = symbol
 # def myfunc2(self): 
  #  print("Hello my name is " + self.name)

e1 = Element("Hydrogen", H, 1) 
print(e1.name) 
print(e1.symbol)
#e1.myfunc2()