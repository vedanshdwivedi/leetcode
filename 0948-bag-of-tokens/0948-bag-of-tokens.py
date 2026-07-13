class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        maxScore = 0
        score = 0
        left, right = 0, len(tokens) - 1
        tokens.sort()
        while left <= right:
            if power < tokens[left] and score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
                maxScore = max(maxScore, score)
            elif power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
                maxScore = max(maxScore, score)
            else:
                break
        return maxScore