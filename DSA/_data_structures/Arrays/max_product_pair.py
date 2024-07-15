import numpy as np 

myArray  = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def max_product_pair(arr):
    maxProduct = 0 
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > maxProduct:
                maxProduct =  arr[i] * arr[j]
                pairs = str(arr[i]) + ","+ str(arr[j])

    print(pairs)
    print(maxProduct)

max_product_pair(myArray)