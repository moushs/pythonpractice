squares={x:x*x for x in range(5)}
print(squares)


#create a dictionary where the keys are even numbers and the values are their cubes
cubes={x:x**3 for x in range(10) if x%2==0}
print(cubes)


#using 2 lists
#create a dictionary from two lists one for keys and one for values
keys=['a','b','c']
values=[1,2,3]
my_dict={keys[i]:values[i] for i in range(len(keys))}
print(my_dict)


original={'a':1,'b':2,'c':3}
reversed_dict={value:key for key,value in original.items()}
print(reversed_dict)


#Filtering items based on value
#create a dictionary where the values are only included if they satisfy a certain condition
#Example:Filter out all entries where the value is less than 5
original={'a':1,'b':6,'c':3,'d':10}
filtered_dict={key:value for key,value in original.items() if value>=5}
print(filtered_dict)


#Transforming Values
#you can transform the values of an existing dictionary while keeping the keys intact
#Example:Multiply each value by 10
original={'a':1,'b':2,'c':3}
transformed_dict={key:value*10 for key,value in original.items()}
print(transformed_dict)


#Nested Dictionary Comorehension
#You can have a dictionary comprehension inside another dictionary comprehension
#Example: Create a dictionary of dictionaries, where each key is associated with another dictionary containing the square and cube of the number
numbers=[1,2,3,4]
nested_dict={x:{'square':x**2,'cube':x**3}for x in numbers}
print(nested_dict)


#Creating a Dictionary from two lists with a condition
#Create a dic from two list
keys=['a','b','c']
values=[1,2,3]
my_dict={keys[i]:values[i] for i in range(len(keys))if i % 2==0}
print(my_dict)


#Creating a dictionary from tuples
#You can use tuples to form key-value pairs for a dictionary
#Example:Convert a list of tuples into a dic
tuples=[('a',1),('b',2),('c',3)]
my_dict={key:value for key,value in tuples}
print(my_dict)


#Example:Handle the missing keys(default value)
#using dictionary comprehension to add default values if the key is missing
#Add a default value if the key is not found in the key
keys=['a','b','c','d']
values=[1,2,3]
my_dict={k:values[i] if i<len(values) else 0 for i,k in enumerate(keys)}
print(my_dict)
