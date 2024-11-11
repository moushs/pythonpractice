#wap to find number to characters and digits in a string
x=input()
digit=0
alpha=0
for i in x:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
print("digit = ",digit)
print("alpha = ",alpha)
