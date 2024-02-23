class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # inputs: array of nums, 
        # return true if any value appears twice
        # return false if every element is distinct

        # i can create a hash and if the element appears more than once i can return true
        myHash = {}
    
        for i in range(len(nums)):
            if nums[i] in myHash:
                return True
            myHash[nums[i]] = 1
        return False


        