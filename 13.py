# Let list 1 and list 2 be two list of integer function sublist()

def sublist(a,b):
    index_a=0
    index_b=0

    len_a=len(a)
    len_b=len(b)
    while index_a<len_a and index_b<len_b:
        if a[index_a]==b[index_b]:
            index_a+=1
            index_b+=1
        else:
            index_b+=1
    return index_a==len_a
print(sublist(a=[15,1,100],b=[20,15,30,50,1,100]))
print(sublist(a=[15,50,20],b=[20,15,30,50,1,100]))