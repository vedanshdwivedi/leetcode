class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        triplets = []
        seen = {}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen[nums[i]] = True
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[left] + nums[right] + nums[i]
                if current == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.append(triplet)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    if current > 0:
                        right -= 1
                    else:
                        left += 1
                    
        return triplets

# nums = [1,2,0,1,0,0,0,0]
# nums = [0,0,0,0,0,1,1,2]
# triplets = [[0,0,0]]
# seen = {0: True, }
# i = 0
# left = 1
# right = 4
# current = 0

            


        