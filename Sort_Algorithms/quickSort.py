def split(list, l, r):
    x = list[l]
    i = l+1
    j = r

    while i < j:
        while x > list[i]:
            i+=1


        while x < list[j]:
            j-=1
        
        if i < j:
            list[i], list[j] = list[j], list[i]

    list[l], list[j] = list[j], list[l]
    return j

def quickSort(list, l, r):
    if l < r:
        m = split(list, l ,r)
        quickSort(list,l,m-1)
        quickSort(list,m+1,r)

    return list

numbers = [7,3,5,4,2,9,4,2,1]

print(quickSort(numbers,0,8))