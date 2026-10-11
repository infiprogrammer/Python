# multiplication table using while loop

multiplier= int (input("enter the multiplier:"))
start= 1
end = int (input("enter the range end:"))
while start <= end:
    result =start* multiplier
    print(f"{start}*{multiplier}={result}")
    start += 1