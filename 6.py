# Find all number which are multiple on 17 but not multiple of 5 between 1 and 100

for a in range (1,101):
  if (a%17==0) and (a%5!=0):
      print(a)