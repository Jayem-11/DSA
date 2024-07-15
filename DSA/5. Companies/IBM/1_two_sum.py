class Solution(object):
    def twoSum(self, nums, target):
        res = {}
       
        for i, num in enumerate(nums):
            diff = target - num
            if diff in res:
                return [res[diff], i ]
            res[num] = i