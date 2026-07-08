class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = -1
        left, right = 0, len(height) - 1
        while left <= right:
            minHeight = min(height[left], height[right])
            distance = right - left
            water = distance * minHeight
            maxWater = max(maxWater, water)
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