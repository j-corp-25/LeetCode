# Last updated: 10/22/2025, 12:09:23 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # implementing binary search
        # nums = [-1,0,3,5,9,12] ,target = 9
        # find the middle index
        # compare the target to the middle index value 
        # then check if target  is greater than middle index or less
        # if target is greater than middle index value 
        #  middle index = len(nums) // 2 = 3, index = 2 , 3 , target = 9
        # [5,9,12] 
        # len(nums) // 2 = 1, index = 1 , val = 9 , target = 9
        # the middle index value == target, then return middle index, 
        
        # use two pointers 
        # [-1, 0, 3 , 5, 9,  12], target = -1
        #   l  r   m           
        #   0  1  2   3  4    5
        # 0 + 1 // 2 = 4 

        # [1,2,3]  target = 4
        l = 0  # 2
        r = len(nums) - 1  # 2
        
        while l <= r:  # 0 < 2
              # m = ( 0 +  2) // 2, m = 1
            m = (l + r) // 2 
             
            if target == nums[m]:
              return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
                
        return -1
        
            
            
            

             



        


        