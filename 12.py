# program for simple caluculations

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select operation:")
print("1-add,2-subtract,3-multiply,4-divide")
c=input("Enter choice (1/2/3/4):")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if c=="1":
    print(n1,"+",n2,"=",add(n1,n2))
elif c=="2":
    print(n1,"-",n2,"=",subtract(n1,n2))
elif c=="3":
    print(n1,"*",n2,"=",multiply(n1,n2))
elif c=="4":
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("Invalid input")