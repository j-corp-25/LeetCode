# Last updated: 10/22/2025, 12:08:57 AM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=0
        r=word.find(ch)
        word=list(word)
        while l < r:
            word[l],word[r]=word[r],word[l]
            l += 1
            r -= 1
        return "".join(word)



        
        