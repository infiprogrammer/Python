multiplier = int(input("enter the multiplier:"))
start = 1 
end = int(input("enter thr range:"))
while start <= end:
    result = start*multiplier
    print(f"{multiplier}*{start}={result}")
    start += 1