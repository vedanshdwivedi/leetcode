class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [y*y for y in sorted([abs(x) for x in nums])]
        
        
        
        