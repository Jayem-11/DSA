# solving fibonacci with top down memoization

def fibmemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        return fibmemo(n-1, memo) + fibmemo(n-2, memo)


# solving using bottom down iteration

def fibit(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n-1]


print(fibit(6))
