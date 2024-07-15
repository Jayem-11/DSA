class Solution(object):

    def productExceptSelf(self, nums):
        answer = (len(nums)) * [1]
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *=  nums[i]

        for j in range(len(nums)-1,-1,-1):
            answer[j] *= postfix 
            postfix *= nums[j]
          
        return answer
       