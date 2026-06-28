class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = {0: 1}
        subarrayCount = 0
        total = 0
        for i, num in enumerate(nums):
            total += num
            required = total - k
            requiredCount = prefixSumCount.get(required, 0)
            subarrayCount += requiredCount
            prefixSumCount[total] = prefixSumCount.get(total, 0) + 1

        return subarrayCount


# nums = [1,2,3]
# k = 3
# prefixSumCount = {0: 1, 1: 1, 3: 2}
# subarrayCount = 1
# total = 3
# required = 0
# requiredCount = 1
# i = 1
# num = 2