class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        # Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2

# result  = 2

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                currentTotal = abs(arr1[i] - arr2[j]) 
                if currentTotal <= d:
                    result -= 1
                    break
            result += 1
        return result

        
                                        #     4      - 10 = 6
                                #     4 - 9 = 5
                                #     |4-9|=5 > d=2 
                                #    |4-1|=3 > d=2 
                                #       |4-8|=4

                                #       |5-10|=5 > d=2 
                                #         |5-9|=4 > d=2 
                                #         |5-1|=4 > d=2 
                                #         |5-8|=3 > d=2

                                #         |8-10|=2 <= d=2
                                #             |8-9|=1 <= d=2
                                #             |8-1|=7 > d=2
                                #             |8-8|=0 <= d=2
        # arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
        # when you compare each arr1[i] to each arr2[j], all values must pass condition to increase result, or increase = 0
        # initialize a count = 0

#         Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1

# result = 0 
# arr1[0]
# 2 - (-5) = 7 >    d = 6  true
# 2 - -2  = 4 < d false
# 2 - 10 = 8 > true
# 2 - - 3 = 5  < d false
# 2 - 7 = 5 < d false


# arr1[1]
# 1 - -5 = 6
# 1 - -2 = 3  < d = false
# 1 - 10 = 9 > d = true
# 1 - -3 = 4 < d = false
# 1 - 7 = 6  < d = false

# result += 1
# arr1[2]
# 100 - - 5 = 105 true
# 100 - -2 = 102 tre
# 100 - 10 = 90 treu 
# 100 - - 3 = 103 true
# 100 - 7 = 93 true


# arr1[3]
# 3 -- 5 =  8 > d = true
# 3 -- 2 = 5 < d = false
# 3 - 10 = 8 > d = true
# 3 -- 3 = 6  false
# 3 - 7 = 4 < = d false



# array1 = [4,5]
# array2 = [10,9]
# d = 2
# i = 1
# j = 1
# currentTotal = 6
# for loop i  to iterate for each value in the first arr1 ()
     
     # for loop j in the seccond array

        # currentTotal = abs(arr1[i] - arr2[j]) 
                            # (4 - 9) = 5
                        
        # if currentTotal < d:
        # break




         