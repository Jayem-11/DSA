def merge(list, l , m, r):
    n1 = m - l+1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = list[l+i]

    for j in range(0, n2):
        R[j] = list[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i+=1
        else:
            list[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        list[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        list[k] = R[j]
        j+=1
        k+=1


def merge_sort(list, l, r):
    if l < r:
        m = (l+(r-1))//2
        merge_sort(list,l,m)
        merge_sort(list,m+1,r)
        merge(list,l,m,r)

    return list

numbers = [2,1,7,6,5,3,4,9,8]

print(merge_sort(numbers,0,8))