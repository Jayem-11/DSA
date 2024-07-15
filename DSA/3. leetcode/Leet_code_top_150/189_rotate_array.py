def rotate1(nums, k):
    for j in range(k):
        temp = nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                nums[i] = temp
            else:
                nums[i] = nums[i-1]

def rotate2(nums, k):
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
