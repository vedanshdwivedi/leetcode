class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz_index = 0
        cur_index = 0
        while cur_index < len(nums):
            if nums[cur_index] != 0:
                nums[nz_index] = nums[cur_index]
                nz_index += 1
            cur_index += 1
        for i in range(nz_index, len(nums)):
            nums[i] = 0

        
        
        