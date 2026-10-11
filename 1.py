# A python program to find area of triangle.

a = float(input("please enter the first side of triangle:"))
b = float(input("please enter the first side of triangle:"))
c = float(input("please enter the first side of triangle:"))
perimeter = a+b+c
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("\n python the perimeter of triangle =%0.2f"% perimeter)
print(" the semi perimeter of triangle =%0.2f"% s)
print("the area of a triangle =%0.2f"%area)