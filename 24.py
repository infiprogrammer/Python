# What is the value of second after executing the following line ?

first="kaleidoscope"
second=""
print(len(first)-1)
for i in range(len(first)-1,-1,-2):
    print(first[i])
    second=first[i]+second
    print('second=',second)
    print(second)