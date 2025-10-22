# Last updated: 10/22/2025, 12:09:34 AM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mySet = set()
        result = []

        for num in nums:
            if num in mySet:
                result.append(num)
            else:
                mySet.add(num)

        return result