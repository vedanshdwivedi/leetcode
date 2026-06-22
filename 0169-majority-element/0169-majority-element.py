class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxElement = float('inf')
        maxCount = 0
        cache = {}
        for num in nums:
            numCount = cache.get(num, 0) + 1
            if maxCount < numCount:
                maxElement = num
                maxCount = numCount
            cache[num] = numCount
        return maxElement
        