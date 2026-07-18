class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = 1000000
        curSum = nums[0]
        if curSum >= target:
            return 1
        left= 0
        for right in range(1, len(nums)):
            curSum += nums[right]
            while curSum >= target:
                minLen = min(minLen, right - left + 1)
                curSum -= nums[left]
                left += 1
        return minLen if minLen < 1000000 else 0


            
            


# minLen = 4
#         0 1 2 3 4 5
# nums = [2,3,1,2,4,3]
# target = 7
# left = 1
# right = 5 (upto 5)
# curSum = 7

