class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        r = len(nums) - 1
        l = r - 1
        return ((nums[r] - 1) * (nums[l] - 1))

        