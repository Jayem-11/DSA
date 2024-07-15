# Top down

def number_factor(n, dp):

    if n in (0, 1, 2):
        return 1

    if n == 3:
        return 2

    if n in dp:
        return dp[n]
    else:
        return number_factor(n-1, dp) + number_factor(n-3, dp) + number_factor(n-4, dp)


tempdict = {}
print(number_factor(5, tempdict))


# bottom up approach

def bottom_number_factor(n):
    dp = [1, 1, 1, 2]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-3] + dp[i-4])
    return dp[n]


print(bottom_number_factor(5))
