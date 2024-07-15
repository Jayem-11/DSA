def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            goal = i 

    return goal == 0

def jump(nums):
        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
               farthest = max(farthest, i+ nums[i])
            l = r + 1
            r = farthest
            res +=1
        return res