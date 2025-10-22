# Last updated: 10/22/2025, 12:09:45 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        windowStart = 0
        windowSum = 0
        
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            
#             go into the while loop if windowSum is greater than teh target
            while windowSum >= target:
#                 make the window inclusive by inclusing all the elements
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1
            
#             if the minLength is still infinity then return 0
        if minLength == inf:
            return 0
        
        return minLength
                