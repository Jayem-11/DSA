
def binary(n):
    assert int(n)== n, "N must be a positive interger"
    if n == 0:
        return 0
    return (n % 2) + 10 * binary(int(n/2))

print(binary(11))