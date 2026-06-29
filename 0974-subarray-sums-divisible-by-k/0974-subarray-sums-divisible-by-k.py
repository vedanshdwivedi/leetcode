class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cache = {0: 1}
        total = 0
        count = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in cache:
                count += cache[remainder]
            cache[remainder] = cache.get(remainder, 0) + 1
        return count

# [4,5,0,-2,-3,1]
# k = 5
# cache = {}