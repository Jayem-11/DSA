class Solution(object):
    def maxSubarraySumCircular(self, nums):
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)

            total+=n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax
