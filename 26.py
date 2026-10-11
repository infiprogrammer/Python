# Here is a function to compare the smallest of three input ? 
def min3(x,y,z):
    if x<=y and x<=z:
        minimum=x
    elif y<=z and y<=x:
        minimum=y
    elif z<=x and z<=y:
        minimum=z
    return(minimum)
print(min3(12,18,3))
#print(min3(x:12,y:18,z:4))