#create a list using for loop

a=[10,20,30,40,50]
for i in a:
  print(i,end=" ")


#how to check whether the element is present in the list or not

a=[10,20,30,40,50]
for i in a:
  if i==30:
    print("present")
    break
else:
  print("not present")


#how to check whther the element is present in the list using while loop
a=[10,20,30,40,50]
i=0
while i<len(a):
  if a[i]==30:
    print("present")
    break
  i+=1
else:
  print("not present")


#print the elements of a list using while loop
a=[10,20,30,40,50]
i=0
while i<len(a):
  print(a[i],end=" ")
  i+=1


#write a python code to find the index value of a number 30 in the list a(a=[10,20,30,40])
a=[10,20,30,40]
for i in range(len(a)):
  if a[i]==30:
    print(i)
    break
else:
  print("not present")


#write a python code to find the index value of a number 30 in the list a(a=[10,20,30,40]) is it possible without using loop
a=[10,20,30,40]
if 30 in a:
  print(a.index(30))


a=[10,20,30,40]
print(a[i])


#create a list of many elements
a=[10,20,30,40,50,60,70,80,90,13,56,23,56,35,53,67,33,78]
len(a)
a[len(a)-1]


list_1=[10,43,24,34,67,32,22,67,43,77,89]
list_1[-8]


list_1=[10,43,24,34,67,32,22,67,43,77,89]
list_1[-2]


information=[1,"ABC",84.9,'a']
print(information)
information[1]


#add mousumi in the following list but each character of "mousumi" should be separated
information=[1,"ABC",84.9,'a']
information.append("mousumi")
print(information)
information += "mousumi"
print(information)
information *= 2
print(information)
information[1]="xyz"
print(information)
information[0:3]
information[:0]


i=[1,'ABC',84.9,'a','h','e','l','l','o']
i[::3]


student_2=[2,'STU',8.58,"Female","INDIA","9876543210"]
student_2[-1::-3]


student_2[::2]

#how to print a number 100 times
number=input("enter your number")
print(number*100)

#write a python code to create a list of 10 odd elements without using decision making statements
odd_list=[]
for i in range(1,20,2):
  odd_list.append(i)
print(odd_list)


#write a python code to create a list of 1 to 10 elements and from the list created ,create another list with only odd values
odd_list=list(range(1,11))
print(list(odd_list))
for i in range(1,11,2):
  if i%2!=0:
    odd_list.append(i)
print(odd_list)

list_1=list(range(1,11))
odd=list_1[::2]
print(list_1)
print(odd)

even=list_1[1::2]
print(even)

#create a 2 list and add the elements of both the list
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list1+list2
print(list3)

i=input("enter the string")
list2=list(i)
print(list2)



