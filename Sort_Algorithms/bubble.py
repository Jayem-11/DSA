numbers = [1,3,5,7,2,4,9,8,6]

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
    print(nums)


bubble_sort(numbers)