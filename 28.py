# Here is a function to compute the second largest value list ?
def secondmax(l):
    (a,b) = (0,0)
    a = max(l)
    while a in l:
        l.remove(a)
        print(l)
        if len(l)==0:
            return a
        else:
            b = max(l)
            return(b)

x=[56,23,17,89,98]
print(secondmax(x))