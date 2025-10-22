# Last updated: 10/22/2025, 12:08:49 AM
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        Str = list(s)

        while l < r:
            left_let = ord(Str[l])
            right_let = ord(Str[r])
            if Str[l] == Str[r]:
                l += 1
                r -= 1
            elif Str[l] != Str[r] and left_let < right_let:
                Str[r] = Str[l]
                l += 1
                r -= 1
            else:
                Str[l] = Str[r]
                l += 1
                r -= 1
            
        return "".join(Str)
        