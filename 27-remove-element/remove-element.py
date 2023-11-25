class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
            # if the current value at the index does not equal the val then proceed
                nums[k] = nums[i]
                # use the value of current k for nums array
                k += 1
        return k


        