class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mySet = set()
        for number in nums1:
            if number in nums2:
                mySet.add(number)
        return mySet

        