class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        k = 0
        for i in range(len(nums)):
            if (((nums[i] + diff) in nums) and ((nums[i] + 2*diff) in nums)):
                k += 1
        return k


        