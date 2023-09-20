class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myIndex = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in myIndex:
                return [myIndex[diff], i]
            myIndex[num] = i