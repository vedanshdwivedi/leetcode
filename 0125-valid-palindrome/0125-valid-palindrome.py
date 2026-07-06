class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [a.lower() for a in list(s) if a.isalnum()]
        beg = 0
        end = len(x) - 1
        while beg <= end:
            if x[beg] != x[end]:
                return False
            beg += 1
            end += -1
        return True
        