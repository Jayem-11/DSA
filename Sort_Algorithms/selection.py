numbers = [7,3,5,1,2,4,9,8,6]

def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(i+1 , len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i],num[min_index] = num[min_index] , num[i]
    print(num)

selection_sort(numbers)

