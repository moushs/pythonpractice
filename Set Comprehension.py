#set comprehension
squares={x**2 for x in range(5)}
print(squares)



numbers=[1,2,3,4,5]
squared_numbers={number**2 for number in numbers}
print(squared_numbers)



numbers=[1,2,3,4,5]
even_numbers={number for number in numbers if number%2==0}
print(even_numbers)



words=["apple","banana","cherry","lyn"]
vowels={'a','e','i','o','u'}
vowel_words={word for word in words if any(letter in vowels for letter in word)}
print(vowel_words)



#eliminating duplicates
duplicates=[1,2,3,3,4,5,1,6]
unique_squares={x**2 for x in duplicates}
print(unique_squares)



text="Hello World"
uppercase_letters={char.upper() for char in text if char.isalpha()}
print(uppercase_letters)
