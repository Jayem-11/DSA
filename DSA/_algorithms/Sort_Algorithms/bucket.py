import math


def insertion(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    # print(list)


def bucket(list):
    Number_of_buckets = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []

    for i in range(Number_of_buckets):
        arr.append([])

    for j in list:
        index = math.ceil(j*Number_of_buckets/maxValue)
        arr[index-1].append(j)

    for i in range(Number_of_buckets):
        insertion(arr[i])

    k = 0
    for i in range(Number_of_buckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list


numbers = [7, 3, 5, 1, 2, 4, 9, 8, 6]

print(bucket(numbers))
