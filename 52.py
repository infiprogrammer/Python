# '''A list is decreasing if each element is strictly smaller than the preceone.
# For instance [],[7],[11,8]and[89,63,44,19,3] are not. 
# Here is a recursive function to check if a list is decreasing.''' 
def decreasing(l):
    if l==[] or len(l)==1:
        return(True)
    else:
        return(l[0] > l[1] and decreasing(l[1:]))

print(decreasing([11,8,7,6,3,1,31]))
print(decreasing([18,4,3]))
print(decreasing([]))
print(decreasing([5]))