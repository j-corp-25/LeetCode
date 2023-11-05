class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charFreq = {}
        isMatch = 0
        windowStart = 0

        for char in s1:
            if char not in charFreq:
                charFreq[char] = 0
            charFreq[char] += 1

        for windowEnd in range(len(s2)):
            rightChar = s2[windowEnd]
            if rightChar in charFreq:
                charFreq[rightChar] -= 1
                if charFreq[rightChar] == 0:
                    isMatch += 1
                
            if windowEnd >= len(s1) - 1:
                if isMatch == len(charFreq):
                    return True

                leftChar = s2[windowStart]
                windowStart += 1
                if leftChar in charFreq:
                    if charFreq[leftChar] == 0:
                        isMatch -= 1
                    charFreq[leftChar] += 1
        return False
        