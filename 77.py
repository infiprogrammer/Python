"""Given two positive integer N and X,where N is the number of total patient arrives
also doctor will give only 10 minutes to each patient the task is to calculate the time 
(in minutes)the last patient needs to wait.

#example1: input N=4,x=5   output:15
#explation: The arrival time of the patients are 0,5,10 and15 respectively.
when the first three patient are respectively10,20,30.so the waiting time is 30-15=15
n=int(input())"""
N=int(input("enter the total patient:"))
x=int(input("enter time duration:"))
for i in range(N):
    t=0
    if N==1:
        print(t)
    else:
        t=(N-1)*(10-x)
print(t)