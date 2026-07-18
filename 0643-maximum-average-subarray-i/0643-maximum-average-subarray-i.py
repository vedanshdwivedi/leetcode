class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -float('inf')
        left, right = 0, k-1
        curSum = None
        while right < len(nums):
            if left == 0:
                curSum = sum(nums[:right + 1])
                print(curSum)
            else:
                curSum = curSum - nums[left - 1] + nums[right]
            maxAvg = max(maxAvg, curSum/k)
            left += 1
            right += 1
        return maxAvg
