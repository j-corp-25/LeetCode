class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through array
        # check if the first number and the one next to it is equal
        # then switch them
        left = 0
        right = 1

        for i in range(len(nums) - 1):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
        
                