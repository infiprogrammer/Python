#To find GCD of two numbers.
def GCD(x,y):
    if x > y:
        smaller=y
    else:
        smaller=x
        
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            gcd = i
    return gcd
print(GCD(54,81))