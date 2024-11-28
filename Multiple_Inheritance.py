class NormalRoom:
    def calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 300
        elif days > 1 and days <= 5:
            room_rent = 250
        else:
            room_rent = 200
        total_rent = room_rent * no_rooms
        return total_rent

class AcRoom:
    def ac_calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 450
        elif days > 1 and days <= 5:
            room_rent = 300
        else:
            room_rent = 250
        total_rent = room_rent * no_rooms
        return total_rent

class SuiteRoom:
    def suite_calculates(self, no_rooms, days):
        if days == 1:
            room_rent = 550
        elif days >= 5:
            room_rent = 500
        else:
            room_rent = 450
        total_rent = room_rent * no_rooms
        return total_rent

class DerivedClass(NormalRoom, AcRoom, SuiteRoom):
    
    pass  


derived_room = DerivedClass()


normal_rent = derived_room.calculates(2, 3) 
ac_rent = derived_room.ac_calculates(1, 5)   
suite_rent = derived_room.suite_calculates(3, 7) 

print(f"Normal Room Rent: {normal_rent}")
print(f"AC Room Rent: {ac_rent}")
print(f"Suite Room Rent: {suite_rent}")

----------------------------------------------------------------------------------------------------------------------------------------------------------


#write a python program to calculate the salary of the temporary staff using Multilevel Inheritance
#Create a class person which contains a constructor init() and a method display(self).The method displays the name of the person.
#Create another class Staff which inherit Person.It contains a constuctor init() and a method display(self).The method displays Id.
#Create another class Temporarystaff which inherit Staff it also contains a constuctor init() and 2 method display(self), Salary(self).
#The method Salary(self) return the total salary earned . The method display(self) displays number of days, hoursworked and total salary earned.
#salary earned=total hours worked*150
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Staff(Person):
    def __init__(self, name, Id):
        super().__init__(name)
        self.id = Id

    def display(self):
        super().display()
        print("ID:", self.id)


class TemporaryStaff(Staff):
    def __init__(self, name, Id, days, hoursworked):
        super().__init__(name, Id)
        self.days = days
        self.hoursworked = hoursworked

    def Salary(self):
        salary = self.days * self.hoursworked * 150
        return salary

    def display(self):
        super().display()
        print("No of days:", self.days)
        print("No of hours worked:", self.hoursworked)
        print("Total Salary:", self.Salary())



name = input("Enter name: ")
Id = int(input("Enter ID: "))
days = int(input("Enter number of days worked: "))
hoursworked = int(input("Enter hours worked per day: "))

temp_staff = TemporaryStaff(name, Id, days, hoursworked)


temp_staff.display()
