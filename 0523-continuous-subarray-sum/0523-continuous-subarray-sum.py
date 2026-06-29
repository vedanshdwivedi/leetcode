class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in cache:
                requiredIndex = cache[remainder]
                if i - requiredIndex > 1:
                    return True
            if cache.get(remainder) is None:
                cache[remainder] = i
        return False
        

# (prefix[i] - prefix[i - 1]) % k == 0
# prefix[i] % k == prefix[i - 1] % k
# [23, 2, 4, 6, 7] -> [23, 25, 29, 35, 42]
# 23 25 29 35 42 -> 5 1 5 5 0
 