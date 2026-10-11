# To check a given number on string is palindrone or not 

def revers(s):
    return s[::-1]
s = input("enter name or number:")
ans = revers(s)
print(ans)
if ans == s:
    print("palindrome")
else:
    print("non palindrome")
    