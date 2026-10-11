#Implement function name() that takes number input and repeatedly ask the user to enter the first name of a student ia a class.
#when the user enter the empty string,the function should print for every name the number of students with that name.

def names():
    name_counts = {}
    while True:
          name=input("enter next name:")
          if name=="":
            break
          if name is name_counts:
            name_counts[name]+=1
          else:
            name_counts[name]=1
    for name,count in sorted( name_counts.items()):
          if count == 1:
            print(f"there is {count} student named {name}")
          else:
            print(f"there are {count} students named {name}")
print(names())            