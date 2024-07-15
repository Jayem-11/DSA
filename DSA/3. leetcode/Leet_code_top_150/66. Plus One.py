class Solution(object):
    def plusOne(self, digits):
        n = 0
        res = []

        for num in digits:
            n = n * 10 + num
        n = n + 1

        while n > 0:
            res.insert(0,n%10)
            n = n//10
        return res
        