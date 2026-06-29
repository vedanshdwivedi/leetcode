class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        cache = {0: 1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            required = total - goal
            if required in cache:
                count += cache[required]
            cache[total] = cache.get(total, 0) + 1
        return count
        