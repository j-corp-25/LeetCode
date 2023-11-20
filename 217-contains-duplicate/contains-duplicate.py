class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_map = set()
        for num in nums:
            if num in my_map:
                return True
            my_map.add(num)
        return False

        