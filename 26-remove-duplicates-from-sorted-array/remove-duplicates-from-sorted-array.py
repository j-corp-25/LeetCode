class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_dup = 1
        i = 0

        while i < len(nums):
            if nums[next_dup - 1] != nums[i]:
                nums[next_dup] = nums[i]
                next_dup += 1
            i += 1
        return next_dup


        