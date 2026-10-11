s = input()
upper=0 
lower=0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("upper case latter is",upper)
print("lower case latter is",lower)
        
        