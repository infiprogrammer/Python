#""" write a python program that permots the user to enter a list  of first main and store then in a list in a program should disply how many times the letter 'a' appers cwith in the last """

name_list = []
total = 0
while"adding more names":
    name = str(input('please enter name:'))
    name_list.append(name)
    
    tally = name.count('a')
    total += tally
    print("the number of 'a' in current name is :",tally)
    
    if input('Add more name ? y/n:') == 'n':
        break
print(name_list)
print("the number of 'a' is:", total)