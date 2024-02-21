class Solution(object):
    def minSubArrayLen(self, target, nums):
        size = float("inf")
        l,total = 0 , 0

        for r in range(len(nums)):
            total+= nums[r]
            while total >= target:
                size = min(size, (r-l)+ 1)
                total -= nums[l]
                l += 1

        return 0 if size == float("inf") else size

        