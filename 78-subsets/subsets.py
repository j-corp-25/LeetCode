class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #start with an empty array 
        # use the common two for loop to find all possible combinations
        # try to filter out base on index value if its the same, or value?
        # the base will always [], 
        # if the array is length of 1, then will return initialized array with the input array, 
        # no edge case for empty
        # one for loop 
        # for i , in range ...
        # for j in range(i + 1, len(nums))
        # subsets = nums[i:j]
        # backtracking pattern
        # [1,2,3,4]
        # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3], [4], [1,4],[2,4],[1,2,4],[1,3,4], ,[2,3,4], [1,2,3,4]]
        
        result = [[]]
        if len(nums) == 1:
            result.append(nums)
            return result
        
        for i in range(len(nums)):
            for j in range(len(result)):
                result2 = result[j]
                result.append([nums[i]] + result2) 
               
                
                


                 

                


        return result


        