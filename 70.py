#write a python program that prompts the user to enter integer values for each of two list.
# It then display whether the lists are of the same length whether the element in each list sum to the same value,
# and whether there are any value that occur in both lists. 
def get_integer_list(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer_list = list(map(int,user_input.split(',')))
            return integer_list
        except ValueError:
            print("Invalid input.Please enter comma-separated integer.")
        except Exception as e:
            print(f"An unexpected error occurred:{e}")
def analyze_lists():
    list1 = get_integer_list("Enter comma-separated integers for first the list:")
    list2 = get_integer_list("Enter comma-separated integers for the second list:")
    
    if len(list1) == len(list2):
        print("The lists are the same length.")
    else:
        print("The lists are not of the same length.")
        
    if sum(list1) == sum(list2):
        print("The elements in each list sum to the same value")
    else:
        print("The elements in each list do not sum to the same value")
    common_values = set(list1) & set(list2)
    if common_values:
        print(f"There are in both lists:{list(common_values)}")
    else:
        print("There are no common values in both lists:")
analyze_lists()    
    