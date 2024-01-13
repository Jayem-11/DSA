def insertion(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>=0 and key < list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = key
    print(list)

numbers = [7,3,5,1,2,4,9,8,6]

insertion(numbers)