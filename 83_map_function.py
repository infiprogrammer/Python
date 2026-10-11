# Let's  start with a simple example of using map() function
s = ["1", "2", "3", "4"]
res = map(int, s)
print(list(res))

# Let's apply double on every member
def double(x):
    return x * 2

a = [1, 2, 3, 4]

res = list(map(double, a))

print(res)
