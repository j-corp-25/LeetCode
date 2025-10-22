# Last updated: 10/22/2025, 12:09:15 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        maxLength = 0
        oneCount = 0

        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 1:
                oneCount += 1

            while (windowEnd - windowStart + 1 - oneCount) > k:
                if nums[windowStart] == 1:
                    oneCount -= 1
                windowStart += 1

            maxLength = max(maxLength,windowEnd - windowStart + 1)
        return maxLength
        