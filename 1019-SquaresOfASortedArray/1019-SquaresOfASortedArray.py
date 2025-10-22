# Last updated: 10/22/2025, 12:09:18 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        new_Array = [(x * x) for x in nums]
        return sorted(new_Array)
        
        


        