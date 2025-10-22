# Last updated: 10/22/2025, 12:08:44 AM
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        for start in range(len(nums)):
            current_or = 0
            for end in range(start, len(nums)):
                current_or |= nums[end]
                if current_or >= k:
                    min_length = min(min_length, end - start + 1)
                    break
        return min_length if min_length != float('inf') else -1
        