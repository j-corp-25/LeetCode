class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}
        maxLength = 0
        windowStart = 0
        maxCount = 0

        for windowEnd in range(len(s)):
            endChar = s[windowEnd]
            if endChar not in charFreq:
                charFreq[endChar] = 0
            charFreq[endChar] += 1

            maxCount = max(maxCount, charFreq[endChar])

            while (windowEnd - windowStart + 1) - maxCount > k:
                startChar = s[windowStart]
                charFreq[startChar] -= 1
                windowStart += 1
            maxLength = max(maxLength,windowEnd - windowStart + 1)
        return maxLength
        