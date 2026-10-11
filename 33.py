# program that accepts a sentence and calculate the no of upper and lower case ?

s=input()
upper=0
lower=0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("upper case letter is",upper)
print("lower case letter is",lower)