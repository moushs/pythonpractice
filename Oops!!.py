#Class Python:-----------------!!!!
class Python:
  def fun(self):
    print("WELCOME TO OOPS CONCEPT")
pyt=Python()
pyt.fun()

#class Car:---------------!!!!
class Car:
    'Common_car'
    car=0
    def __init__(self,name,id):
       self.name=name
       self.id=id
       Car.car+=1
    def printCardata(self):
         print("Name:",self.name,"Id:",self.id)
c=Car("AUDI",2000000)
c.printCardata()

#class Employee:---------------!!!!
class Employee:
  def set_data(self,n,a,s):
    self.name = n
    self.age = a
    self.salary = s
  def display_data(self):
    print(self.name, self.age , self.salary)

e1  = Employee()
e1.set_data("xxxxx" , 26 , 30000)
e1.display_data()

#class Birds:---------------!!!!
class Birds:
    def __init__(self,b1,b2,b3):
        self.b1=b1
        self.b2=b2
        self.b3=b3
    def printdata(self):
        print(self.b1,self.b2,self.b3)
b=Birds("Eagle","Crow","Sparrow")
b.printdata()

#class pos and neg no:---------------!!!!
class Numbers:
    def __init__(self, pos1, pos2, neg1, neg2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.neg1 = neg1
        self.neg2 = neg2

    def printdata(self):
        print("Positive values:", self.pos1, self.pos2)
        print("Negative values:", self.neg1, self.neg2)

#class POs and neg (2):---------------!!!!
class NumberCheck:
    def __init__(self, number):
        self.number = number

    def check_sign(self):
        if self.number > 0:
            return "Positive"
        elif self.number < 0:
            return "Negative"
        else:
            return "Zero"

num = NumberCheck(26)
print(f"The number is {num.check_sign()}.")

#class Car(2):---------------!!!!
class Car:
  'Common_car'
  car=0
  def __init__(self,name,id):
     self.name=name
     self.id=id
     Car.car+=1
  def printCardata(self):
       print("Name:",self.name,"Id:",self.id)
c=Car("AUDI",2000000)
c1=Car("BENZ",3000000)
c2=Car("BMW",1000000)
print("Total Cars:",Car.car)
c.printCardata()
c1.printCardata()
c2.printCardata()

#class test:---------------!!!!
class test:
  def __init__(self):
    self.variable='Car'
    self.Change(self.variable)
  def Change(self,var):
    self.var='Bike'
obj=test()
print(obj.variable)
print(obj.var);


