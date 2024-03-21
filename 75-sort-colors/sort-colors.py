class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # maybe two pointers?
        # it will start at index 0 and then at the end of the nums
        
        


        # two pass solution
        # loop over nums
        # get a count fo values  0 , 1, 2
        # with the count index into nums and make those values equal
        # have three variables with 0 ,1, 2
        # nums.Count(2) = 5
        # check the the count of each 
        # nums[:Count(0)] = 4
    #    [2,0,2,1,1,0]
        num0 = nums.count(0) # 2
        num1 = nums.count(1) # 2
        num2 = nums.count(2) # 2

        for i in range(len(nums)):  # i = 5
            if num0 > 0:  # 0 
                nums[i] = 0 # [0,0,2,1,1,0]
                num0 -= 1 # 0
            elif num1 > 0: # 0
                nums[i] = 1 # [0,0,1,1,1,0]
                num1 -= 1 # 0
            else:
                nums[i] = 2 # [0,0,1,1,2,2]
                num2 -= 1 # 0
            
     


        