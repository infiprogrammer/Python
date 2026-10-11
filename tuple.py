def printtuple(n):
    l = [(i,i**3)for i in range(1,n+1)]
    print(tuple(l))
    print(l)
printtuple(6)