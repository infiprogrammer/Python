#To check a number is prime or not 

a=int(input("enter the number:"))
k=0
for i in range(2,a//2+1):
 if (a%i==0):
    k= k+1
if(k==0): 
 print("prime number")
else:
 print("non prime number")