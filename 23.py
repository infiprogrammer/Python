#consider the following lines of python code ?
x = [589,'big',397,'bash']
y = x[2:]
u = x
w = y
w = w[0:]
w[0] = 357
x[2:3] = [487]
print(x)
print(y)
print(u)
print(w)