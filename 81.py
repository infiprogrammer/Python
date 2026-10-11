#If the string is less than 3,leave it unchanged
#If leength is atleast 3,add 'ing' at the end.
#If the string already end with 'ing' add 'ly' instead.
def add_string(str1):
    n=len(str1)
    if n>2:
        if str1[-3:]=='ing':
            str1+='ly'
        else:
            str1+='ing'
    return(str1)
print(add_string('ab'))
print(add_string('abcde'))
print(add_string('strring'))