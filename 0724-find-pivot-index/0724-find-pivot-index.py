class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for i in range(0, len(nums)):
            rightSum = rightSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        