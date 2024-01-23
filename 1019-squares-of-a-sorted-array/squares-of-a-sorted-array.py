class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        Myarray = []
        for i in range(len(nums)):
            Myarray.append(nums[i] * nums[i])
        Myarray.sort()
        return Myarray

        