class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charFreq = {}
        maxLength = 0
        windowStart = 0

        for windowEnd in range(len(s)):
            endChar = s[windowEnd]

            charFreq[endChar] = charFreq.get(endChar, 0) + 1

            while charFreq[endChar] > 1:
                startChar = s[windowStart]
                charFreq[startChar] -= 1

                if charFreq[startChar] == 0:
                    del charFreq[startChar]
                
                windowStart += 1
            maxLength = max(maxLength,windowEnd - windowStart + 1)

        return maxLength
        