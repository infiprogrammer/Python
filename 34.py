# to check perfect no & generate sum of its division ?

def perfect(n):
    l=[]
    for i in range(1,n//2+1):
        if n%i==0:
            l.append(i)
    s=sum(l)
    print(s,l)
    if s==n:
        return True 
    else:
        return False
print(perfect(6))
print(perfect(28))
print(perfect(12))
print(perfect(9))