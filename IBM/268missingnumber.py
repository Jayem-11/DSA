# my solution 

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
    
        
# solution with most votes
class Solution(object):
    def missingNumber(self, nums):
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)