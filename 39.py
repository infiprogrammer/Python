#function to find to all number in a range which are perfect square

l = int(input("Enter lower range:"))
u = int(input("Enter upper range:"))
a = []

for x in range(l,u+1):
    if(int(x**0.5))**2==x:
       a.append(x)
print(a)