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


class Calculator:
  def add(self,num1,num2):
    self.num1=num1;
    self.num2=num2;
    return self.num1+self.num2
  def sub(self,num1,num2):
    return num1-num2;
class AdvancedCalculator(Calculator):
  def mul(self,num1,num2):
    print("Multiplication:",num1*num2)
  def div(self,num1,num2):
    return num1//num2;
x=AdvancedCalculator()
num1=int(input())
num2=int(input())
print("addition : %d"%(x.add(num1,num2)))
print("subtract",x.sub(num1,num2))
x.mul(num1,num2)
print("floor division: %d"%(x.div(num1,num2)))    

