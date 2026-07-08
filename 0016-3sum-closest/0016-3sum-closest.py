class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minSum = 0
        minDiff = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                curDiff = abs(target - curSum)
                if curDiff < minDiff:
                    minSum = curSum
                    minDiff = curDiff
                if curSum == target:
                    return target
                elif curSum > target:
                    right -= 1
                else:
                    left += 1
                
        return minSum

# nums = [-4,-1,1,2]
# minDiff = 4
# i = 0
# left = 1
# right = 2
# target = 1
# curSum = -3
# curDiff = 4