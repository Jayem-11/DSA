# average case
class Solution(object):
    def fizzBuzz(self, n):
        ans = [0] * n
        for i in range(1,n+1):
            if (i%3 == 0 ) and (i%5 == 0):
                ans[i-1] = "FizzBuzz"
            elif (i%3 == 0 ):
                ans[i-1] = "Fizz"
            elif (i%5 == 0):
                ans[i-1] = "Buzz"
            else:
                ans[i-1] = str(i)
        return ans

# best case

class Solution(object):
    def fizzBuzz(self, n):
        f, b , fb = "Fizz", "Buzz", "FizzBuzz"
        arr = [str(i + 1) for i in range(n)]

        for i in range(2, n, 3):
            arr[i] = f

        for i in range(4, n, 5):
            arr[i] = b

        for i in range(14, n, 15):
            arr[i] = fb

        return arr