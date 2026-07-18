class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        for i in range(k):
            if s[i].lower() in vowels:
                count += 1
        maxCount = count
        left, right = 1, k
        while right < len(s):
            left_char = s[left - 1]
            added_char = s[right]
            if left_char.lower() in vowels:
                count -= 1
            if added_char.lower() in vowels:
                count += 1
            left += 1
            right += 1
            maxCount = max(maxCount, count)
        return maxCount
        