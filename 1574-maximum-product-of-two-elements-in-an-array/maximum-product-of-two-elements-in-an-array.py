class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sort the algorithm
        nums.sort()
        # get the last element and the element before the last with two pointers
        r = len(nums) - 1
        l = r - 1
        return ((nums[r] - 1) * (nums[l] - 1))

        