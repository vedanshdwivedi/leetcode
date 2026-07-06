class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        curEligibleIndex = 0
        curIndex = 0
        while curIndex < len(nums):
            if nums[curIndex] in seen:
                curIndex += 1
            else:
                seen[nums[curIndex]] = True
                nums[curEligibleIndex] = nums[curIndex]
                curIndex += 1
                curEligibleIndex += 1

        return curEligibleIndex

# curIndex = 0 (curIndex < 3)
# curEligibleIndex = 0
# seen = {}
# nums = [1,1,2]