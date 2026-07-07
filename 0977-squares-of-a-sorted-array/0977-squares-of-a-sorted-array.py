class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = [0] * len(nums)
        eligibleIndex = len(nums) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                nums1[eligibleIndex] = nums[right] * nums[right]
                right -= 1
            else:
                nums1[eligibleIndex] = nums[left] * nums[left]
                left += 1
            eligibleIndex -= 1
        return nums1

# nums = [-4,-1,0,3,10]
# nums1 = []
# left = 0
# right = 4