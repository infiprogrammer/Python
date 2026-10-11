# To read a list of word & return the length of the longest ?

def longestword(l):
    l1 = list()
    for i in l:
        l1.append(len(i))
    print(l1)
    return(max(l1))
l = ["mango","kiwi","banana","watermelon","car"]
print(longestword(l))