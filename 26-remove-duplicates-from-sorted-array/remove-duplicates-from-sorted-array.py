class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we need two pointers

        right = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[right - 1]:
                nums[right] = nums[i]
                right += 1
        return right