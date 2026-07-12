class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        eligibleIndex = 0
        left = 0
        for i in range(left, len(nums)):
            if nums[i] == 0:
                nums[eligibleIndex], nums[i] = 0, nums[eligibleIndex]
                eligibleIndex += 1
        left = eligibleIndex
        # print(nums)
        for i in range(left, len(nums)):
            if nums[i] == 1:
                nums[eligibleIndex], nums[i] = 1, nums[eligibleIndex]
                eligibleIndex += 1
        
#         0 1 2 3 4 5
# nums = [0,1]
# eligibleIndex = 0
# left = 1
# i = 1 (1,2,3,4,5)

