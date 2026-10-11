# Program to combine sorted list

# intializing lists
test_list1 = [1, 5, 6, 9, 11, 12]
test_list2 = [3, 4, 7, 8, 10, 16]

# print original list


print("The Orginal list1 is:", (test_list1))
print("The Orginal list2 is:", (test_list2))

test_list1 = test_list1 + test_list2
print(test_list1)
test_list1.sort()

print("the combined sorted list is:",(test_list1))
