# For what value of n would g(57,n) return 7 ?

def g (m,n):
    res=0
    while m>=n:
        res =res+1
        m=m-n
    return (res)
print(g(m=57,n=8))
print(g(m=73,n=9))
