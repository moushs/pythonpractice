class Car:
  def speed(self):
    print("100km")
class Audi(Car):
  def engine(self):
    print("Engine is powerful")
c=Audi()
c.engine()
c.speed()


class Animal:
  def sound(self):
    print("Animal makes sound")
class Dog(Animal):
  def sound(self):
    print("Barks")
class Cat(Animal):
  def sound(self):
    print("Meoww!!!")
dog=Dog()
cat=Cat()
dog.sound()
cat.sound()


x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
class calculate:
    def sum(self,x,y):
      self.x=x
      self.y=y
      print(self.x+self.y)

    def sub(self,x,y):
      self.x=x
      self.y=y
      print(self.x-self.y)

class AdvanceCalculate(calculate):
    def mul(self,x,y):
      self.x=x
      self.y=y
      print(self.x*self.y)

    def div(self,x,y):
      self.x=x
      self.y=y
      print(self.x/self.y)
c=AdvanceCalculate()
c.sum(x,y)
c.sub(x,y)
c.mul(x,y)
c.div(x,y)
