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
