def pow(x,n):
    assert n>=0 and int(n)== n, "N must be a positive interger"
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)

print(pow(5,4))