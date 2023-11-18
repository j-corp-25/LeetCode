class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
# This is the brute force of solving this problem, we compare each element in the array with the next element
# The time complex is O(n^2) because there is a nested loop
# The space complex is constant time because we only need to store a few variables
        # unique_set = set()

        # for num in nums:
        #     if num in unique_set:
        #         return True
        #     unique_set.add(num)
        # return False
# # This uses a set to check if there are any duplicates in the array
# We add a the new number to the set if its not in it in the first place but if it is we can return True
# Time complex is O(n) because we only iterate through the entire thing once 
# The space is O(n) because we are storing the values in the set

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

# This sorts the algo beforehand which is n log n
# when a list is sorted it duplicates appear next to each other so we check if the next element is the same
