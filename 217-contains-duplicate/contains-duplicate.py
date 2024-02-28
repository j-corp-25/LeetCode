class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True

        