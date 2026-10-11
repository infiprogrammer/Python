# Given any 2 strings ,write a function to print them in sorted manner without using inbuilt function.
def print_sorted_strings(str1,str2):
    if str1<str2:
        print(str1)
        print(str2)
    else:
        print(str2)
        print(str1)
string1="Zebra"
string2="apple"
print_sorted_strings(string1,string2)    