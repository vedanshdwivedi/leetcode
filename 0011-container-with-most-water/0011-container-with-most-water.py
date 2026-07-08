class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = -1
        left, right = 0, len(height) - 1
        while left <= right:
            # distance = (right - left)
            # height = min(height[left], height[right])
            # water = distance * height
            water = (right - left) * min(height[left], height[right])
            if water > maxWater:
                maxWater = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater

# height = [1,8,6,2,5,4,8,3,7]
# left = 0
# right = 9
# maxWater
# minHeight = 
# distance = 
# water = 