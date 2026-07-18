class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = {s[0]: 1}
        left, right = 0, 1
        maxLen = 1
        while right < len(s):
            if seen.get(s[right], 0) > 0:
                seen[s[left]] = seen[s[left]] - 1
                left += 1
            else:
                seen[s[right]] = seen.get(s[right], 0) + 1
                right += 1
            maxLen = max(maxLen, right - left)
        return maxLen

# s = pwwkew
# left = 0
# right = 1    (2,3,4)
# maxLen = 1
# seen = {}
