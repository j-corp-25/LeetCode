# Last updated: 10/22/2025, 12:08:48 AM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        c = 0
        l = 0
        r = n-1

        while l < r:
            if nums[l] + nums[r] < target:
                c += r - l
                l += 1
            else:
                r -= 1

        return c
        