class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        el_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[el_index] = nums[i]
                el_index += 1
            
        return el_index

