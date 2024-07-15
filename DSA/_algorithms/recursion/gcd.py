def gcd(x,n):
    assert int(x) == x and int(n)== n ,"Must be an interger"
    if x<0:
        x = -1 * x
    if n<0:
        n = -1 * n
    if n == 0:
        return x
    else:
        return gcd(n, x % n)

print(gcd(48,18))