# PRogram what is the value of f (345) for the function  

def f(x):
    d=0
    y=1
    while y<=x:
        d=d+1
        y=y*3
        print(d,y)
    return(d)
print(f(345))   
    