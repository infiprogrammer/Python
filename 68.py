# to find the greatest from a list of numbers.
x=[]
n=int(input("enter the upper limit:"))

for i in range(0,n):
    a=int(input("Enter the number:"))
    x.append(a)
    
captain=x[0]

for i in range(1,n):
    if x[i]>captain:
        captain=x[i]
print(x)        
        
print("The greatest number is:",captain)