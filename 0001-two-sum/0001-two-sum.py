class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            com = target - num

            if com in cache:
                return [i, cache[com]]
            
            cache[num] = i
                            

        