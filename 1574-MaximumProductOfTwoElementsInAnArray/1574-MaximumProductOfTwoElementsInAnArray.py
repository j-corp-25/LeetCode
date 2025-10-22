# Last updated: 10/22/2025, 12:09:05 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1,max2 = 0,0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)

        