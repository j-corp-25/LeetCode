# Last updated: 10/22/2025, 12:08:56 AM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

        