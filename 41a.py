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
print("the number of 'a' is :",total)