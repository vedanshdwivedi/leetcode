class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        s, t = list(s), list(t)

        for i in range(len(s)):
            if s[i] == "#":
                if len(stackS) > 0:
                    stackS.pop(-1)
            else:
                stackS.append(s[i])

        for i in range(len(t)):
            if t[i] == "#":
                if len(stackT) > 0:
                    stackT.pop(-1)
            else:
                stackT.append(t[i])

        return "".join(stackS) == "".join(stackT)
        
        