class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curEligibleIndex = 0
        curIndex = 0
        while curIndex < len(nums):
            if nums[curIndex] != 0:
                if curEligibleIndex != curIndex:
                    nums[curEligibleIndex] = nums[curIndex]
                curEligibleIndex += 1
            curIndex += 1
        for i in range(curEligibleIndex, len(nums)):
            nums[i] = 0


        
        
        