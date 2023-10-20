
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
    

        max_average = float('-inf')

        windowStart = 0
    

        for windowEnd in range(len(nums)):
            window_sum += nums[windowEnd]
        
        # Slide the window when we've reached size 'k'
            if windowEnd >= k - 1:
        
                max_average = max(max_average, window_sum / k)
            

                window_sum -= nums[windowStart]
    
                windowStart += 1
            
        return max_average

        