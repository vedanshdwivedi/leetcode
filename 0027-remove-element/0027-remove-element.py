class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curEligibleIndex = 0
        curIndex = 0
        while curIndex < len(nums):
            if nums[curIndex] != val:
                nums[curEligibleIndex] = nums[curIndex]
                curEligibleIndex += 1
            curIndex += 1
        return curEligibleIndex
        

# [3,2,2,3]
# []