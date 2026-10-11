# phython program to split a string and join it using different delimiter.
def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

string = 'GPH is the largest polytechnic in haryana state'
list_string = split_string(string)
print(list_string)

new_string = join_string(list_string)
print(new_string)