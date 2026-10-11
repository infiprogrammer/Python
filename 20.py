# What is h(41)-h(40) , given the defination of h. below?
    
def h(n):
    s=0
    for i in range (1,n+1):
        if n%i > 0:
            s=s+1
    return(s)
print(h(41))
print(h(40))
print(h(41)-h(40))