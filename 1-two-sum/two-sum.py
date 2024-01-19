class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in myDict:
                return [myDict[difference],i]
            myDict[nums[i]] = i
       
            


        