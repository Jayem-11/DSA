def sum_of_digits(n):
    assert n>=0 and int(n) == n , "N must be a positive integer"
    if n==0 :
        return 0
    else:
        return sum_of_digits(int(n/10)) + n % 10

print(sum_of_digits(2557))