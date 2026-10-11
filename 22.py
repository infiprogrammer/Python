# Which one of the following to 10 statement genrates an error ?

x=["sun",[17],2,"king",[3,4]]
y=x[0:8]
print(y)
z=x
w=y
z[0]=0
print(z)
y[0]=y[0][0:3]+'k'
print(y)
y[1][0:3]=[5,8]
print(y)
w[4][0]=1000
print(w)
a=(x[4][1]==4)
print(a)
city='chennai'
print(city)
movie="chennai","movie","seen"

print(movie)
title='''hello
everyone'''
print(title)