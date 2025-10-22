# Last updated: 10/22/2025, 12:08:45 AM
class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        
        return score
        