class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through array
        # check if the first number and the one next to it is equal
        # then switch them
        left = 1
        
        for r in range(1,len(nums)):
            if nums[r] != nums[r - 1]:
                nums[left] = nums[r]
                left += 1
        return left
        
                