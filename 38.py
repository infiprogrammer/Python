# string find () method

word = 'python is powerful'

result = word.find('python')
print("substring'python' found at index:",result)

result = word .find('is')
print("substring'is'found at index:",result)

if word.find('Hisar') != -1:
    print("contains given substring")
else:
    print("Doesn't contain given substring")
    