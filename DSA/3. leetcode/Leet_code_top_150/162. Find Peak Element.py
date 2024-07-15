class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1

        while l < r-1:
            m = (l+r) / 2
            if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                return m
            if nums[m] < nums[m+1]:
                l = m +1
            else:
                r = m-1

        return l if nums[l] >= nums[r] else r

    



        