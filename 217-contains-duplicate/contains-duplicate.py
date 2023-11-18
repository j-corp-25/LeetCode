class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        unique_set = set()

        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False

# This is the brute force of solving this problem, we compare each element in the array with the next element
# The time complex is O(n^2) because there is a nested loop
# The space complex is constant time because we only need to store a few variables