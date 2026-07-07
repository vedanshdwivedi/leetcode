class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            calSum = numbers[left] + numbers[right]
            if calSum == target:
                return [left + 1, right + 1]
            elif calSum > target:
                right -= 1
            else:
                left += 1     

# numbers = [2,7,11,15]
# target = 9
# left = 0
# right = 2
# calSum = 17