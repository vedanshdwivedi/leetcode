class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        endIndex = len(nums) - 1
        for i, num in enumerate(nums):
            total += num
            nums[i] = total
        for i, num in enumerate(nums):
            rightSum = nums[endIndex] - num
            leftSum = 0 if i == 0 else nums[i - 1]
            if leftSum == rightSum:
                return i
        return -1
        
        
# [1,7,3,6,5,6]
# [1,8,11,17,22,28]
# leftSum = 
# rightSum = 
# i = 0
# num = 1