import numpy as np

myArray  = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

# time complexity O(n^2)
def unique(arr):
    duplicates = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicates += 1
    if duplicates == 0:
        print("unique")
    else:
        print("Duplicates present") 

# unique(myArray)

# time complexity O(n)

def isUnique(arr):
    a = []
    for i in arr:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isUnique(myArray))