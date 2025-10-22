# Last updated: 10/22/2025, 12:09:16 AM
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0, len(tokens) - 1
        current_score = max_score = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                current_score += 1
                max_score = max(max_score, current_score)
                l += 1
            elif current_score >= 1:
                power += tokens[r]
                current_score -= 1
                r -= 1
            else:
                break
        return max_score
        