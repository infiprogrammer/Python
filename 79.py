#In a given array,find the count of given integer n in the array.

def count_occurrences(arr,n):
    count=0
    for x in arr:
        if x==n:
            count+=1
    return count
array=[1,2,2,3,4,2,5]
number_to_count=2
result=count_occurrences(array,number_to_count)
print(f"The number {number_to_count} appears {result}times in the array.")