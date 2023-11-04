
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = 0
        maxSum = float('-inf')
        windowStart = 0
        
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            
            if windowEnd >= k - 1:
                
                maxSum = max(maxSum, (windowSum/k))
                windowSum -= nums[windowStart]
                windowStart += 1
                
        return maxSum
            