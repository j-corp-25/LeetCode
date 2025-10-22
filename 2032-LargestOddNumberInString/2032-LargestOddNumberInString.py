# Last updated: 10/22/2025, 12:08:55 AM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1

        # iterate from right, then keep moving left as each number is not odd
        while i >= 0:
            # if this equals 1 it will be truthy else, if its 0 it will falsey then dexrease
            if int(num[i]) % 2:
              # start will b 0, and it will end at the latest number, since its exclusive of last number you need to add one
                return num[:i + 1]
            i -= 1
        return ""
        