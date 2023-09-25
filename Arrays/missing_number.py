# Find missing number in an integer array of 1 to n

mylist = [1,2,3,4,5,6,8,9,10]

def missing(list, n):
    sum1= n*(n+1)/2
    sum2= sum(list)
    print(sum1-sum2)

missing(mylist,10)