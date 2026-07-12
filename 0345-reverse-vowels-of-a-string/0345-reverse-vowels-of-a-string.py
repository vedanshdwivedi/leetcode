class Solution:
    def isVowel(self, s: str) -> bool:
        return s.lower() in {'a', 'e', 'i', 'o', 'u'}

    def reverseVowels(self, s: str) -> str:
        vowelIndices = []
        for i in range(len(s)):
            if self.isVowel(s[i]):
                vowelIndices.append(i)
        left, right = 0, len(vowelIndices) - 1
        s = list(s)
        # print(vowelIndices)
        while left <= right:
            s[vowelIndices[left]], s[vowelIndices[right]] = s[vowelIndices[right]], s[vowelIndices[left]]
            left += 1
            right -= 1
        return "".join(s)


# IceCreAm 
# vowelIndices = [0,2,5,6]
# AceCreIm 