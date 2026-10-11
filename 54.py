#The function will print the local x,them the code will print the global x.
x=300
def myfunc():
    x=200
    print(x)
    
myfunc()
print(x)