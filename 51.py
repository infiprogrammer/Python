# to find maximum of 4 numbers.
def max4(w,x,y,z):
    if w >=x and w >=y and w>=z:
        maximum = w
    elif x >=y and x>=z:
        maximum = x 
    elif y>=z:
        maximum = y
    else:
        maximum = z
    return(maximum)
print(max4(28,14,47,2))