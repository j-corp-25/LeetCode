class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        new_Array = [(x * x) for x in nums]
        return sorted(new_Array)
        
        


        