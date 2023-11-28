class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two pointers, both  at beginning and then compare current with the next
        # if theres a zero then swap current index with previous index





        # Start search_zero at 1
        search_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current element with the previous non-zero element
                nums[i], nums[search_zero] = nums[search_zero], nums[i]
                search_zero += 1


        