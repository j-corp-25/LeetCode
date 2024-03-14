class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # [0,0,1,0,0,0,1,1] = 
        # loop through the numbers
        
        
        #  0   1   2   3   4   5  6   7    8   9
        # [0,  0,  0,  0,  0,  1,  1,  1,  1 , 1]
        # -1,  -2, -3, -4, -5, -4, -3, -2, -1,  0
        # i = 0 # 1
        # maxV = 2
        # myHash = { 
        #     0: -1
        #    -1: 0,
        #    -2: 1,
        #    -3: 2,
        #    -4: 3,
        #    -5: 4,
            

        # }
        # index - hash[count]     
        #6 - 2 = 4 
        #5 - 3 = 2
        #7 - 1 = 6
        #8 - 0 = 8
        #9 - (-1) = 10

        myHash = {0: -1}
        longestC = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            elif nums[i] == 1:
                count += 1
            
            if not count in myHash:
                myHash[count] = i
            else:
              longestC = max(i - myHash[count], longestC)
        return longestC


                


            





        