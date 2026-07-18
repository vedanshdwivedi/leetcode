class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = list(s)
        maxCount = 0
        left, right = 0, k-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        count = 0
        while right < len(s):
            if left == 0:
                for i in range(left, right + 1):
                    if s[i] in vowels:
                        count += 1
            else:
                left_char = s[left - 1]
                added_char = s[right]
                if left_char in vowels:
                    count -= 1
                if added_char in vowels:
                    count += 1
            left += 1
            right += 1
            maxCount = max(maxCount, count)
        return maxCount
        