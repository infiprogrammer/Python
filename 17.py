# Program to display the fibanacii sequence upto bn term

nterm = int(input("how many term?"))
n1=0
n2=1
count=0
if nterm <= 0:
    print("please enter a postive integer")
elif nterm == 1:
    print("fibonacci sequence upto",nterm,":")
    print(n1)
else:
    print("fibonacci sequence upto",nterm,":")
    while count < nterm:
        print(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3
        count +=1
    