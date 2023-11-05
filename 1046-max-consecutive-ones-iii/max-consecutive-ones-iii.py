class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        maxLength = 0
        zeroCount = 0

        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 1:
                zeroCount += 1

            while (windowEnd - windowStart + 1 - zeroCount) > k:
                if nums[windowStart] == 1:
                    zeroCount -= 1
                windowStart += 1

            maxLength = max(maxLength,windowEnd - windowStart + 1)
        return maxLength
        