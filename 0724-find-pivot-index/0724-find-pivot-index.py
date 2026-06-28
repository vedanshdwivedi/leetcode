class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for i, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return i

            leftSum += num
        return -1
        
        
        
# [1,7,3,6,5,6]
# [1,8,11,17,22,28]
# leftSum = 
# rightSum = 
# i = 0
# num = 1