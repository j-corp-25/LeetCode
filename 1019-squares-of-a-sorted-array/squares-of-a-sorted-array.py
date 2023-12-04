class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        start,end = 0,len(nums) - 1

        while start <= end:
            if abs(nums[start] * nums[start]) > abs(nums[end] * nums[end]):
                result.insert(0,nums[start] * nums[start])
                start += 1
            else:
                result.insert(0,nums[end] * nums[end])
                end -= 1
        return result
        