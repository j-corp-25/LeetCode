class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input array, input target - int
        # find the index of two values that add to target
        # method:
        # create a empty hash to
        myMap = {}
        # create a loop that will iterate through the numbers and then check if the difference is inside the  hash
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myMap:
                return [myMap[diff],i]
            myMap[nums[i]] = i

        # if it is then return the indexes