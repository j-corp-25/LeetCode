# Last updated: 10/22/2025, 12:09:37 AM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num in mySet:
                return num
            else:
                mySet.add(num)