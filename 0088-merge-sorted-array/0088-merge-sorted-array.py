class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        resIndex = m + n - 1
        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[resIndex] = nums1[p1]
                p1 -= 1
            else:
                nums1[resIndex] = nums2[p2]
                p2 -= 1
            resIndex -= 1
        if p2 > -1:
            for i in range(p2, -1, -1):
                nums1[resIndex] = nums2[p2]
                resIndex -= 1
                p2 -= 1

        
        