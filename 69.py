# To find LCM of 2 number.
def LCM(a,b):
    lar=max(a,b)
    small=min(a,b)
    i=lar
    
    while(1):
        if (i%small==0):
            return i
        i=i+lar
print(LCM(14,8))
