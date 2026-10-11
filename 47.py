n1,n2 = 0,1
total = 0
while True:
    print(n1,n2)
    n1,n2=n2,n1+n2
    if n2 >= 50:
        break
if n2%2 == 0:
    total += n2
print(total)
