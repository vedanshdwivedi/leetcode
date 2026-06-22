class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz_index = cur_index = 0
        max_index = len(nums)
        while cur_index < max_index:
            if nums[cur_index] != 0:
                nums[nz_index] = nums[cur_index]
                nz_index += 1
            cur_index += 1
        for i in range(nz_index, max_index):
            nums[i] = 0

        
        
        