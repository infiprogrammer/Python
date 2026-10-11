# starting with any positive integer n collatz sequence is defined. 
# coresponding to n as the number formed by the following operation.
# if n is even then n=n/2. if n is odd ,then n=3*n+1.
# repeat above steps until it becoms 1.
# program to print collatz sequence.

def printcollatz(n):
    while n != 1:
        print(n,end=',')
        if n &1:
            n=3*n+1
        else:
            n=n//2
    print(n)
printcollatz(9)