# Last updated: 10/22/2025, 12:09:44 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True 
        