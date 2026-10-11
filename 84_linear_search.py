# linear Search

def search(list1, key):
    found = False
    for i in range(len(list1)):
        if list[i] == key:
            found = True
            return f"key found at index", i
    if not found:
        return f"key not found"


list1 = [17, 56, 93, 4, 18, 54]
key = int(input("Enter the key element: "))
print(search(list1,key))
