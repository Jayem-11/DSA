def removeDuplicates(nums) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


nums =  [1,1,2] # Input array
expectedNums = [1,2] # The expected answer with correct length

k = removeDuplicates(nums) #Calls your implementation

assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

