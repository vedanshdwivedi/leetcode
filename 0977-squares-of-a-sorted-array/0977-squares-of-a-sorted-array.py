class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                nums1.append(nums[right] * nums[right])
                right -= 1
            else:
                nums1.append(nums[left] * nums[left])
                left += 1
        return nums1[::-1]