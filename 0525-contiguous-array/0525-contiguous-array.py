class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums_mod = [-1 if x == 0 else x for x in nums]
        total = 0
        seen = {0: -1}
        maxLen = 0
        for i, num in enumerate(nums_mod):
            total += num
            if total in seen:
                requiredIndex = seen[total]
                maxLen = max(maxLen, i - requiredIndex)
            if total not in seen:
                seen[total] = i
        return maxLen
            
# nums = [0,1]
# nums_mod = [-1, 1]
# seen = {-1: 0}
# maxLen = -1
# i = 1
# num = 1
# total = 0


