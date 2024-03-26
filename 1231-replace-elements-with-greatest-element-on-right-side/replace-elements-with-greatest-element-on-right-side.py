class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initialyze and empty array =  result = []
        # loop through the arr 
        #  [17,18,5,4,6,1]
        #    0,1,2,3,4,5
            # current = max()
            # arr[i:]
        # max from the point where i is till the end of the array
        # max [i:]  
        # result.append(current)
        # then append it the array we initialized from the start
        # 
        # do it for each value
        # append -1 after the loop
        # if array length is 1 then return -1
        if len(arr) == 1:
            return [-1]

        result = [0] * len(arr)
        maxValue = -1
        # [17,18,5,4,6,1]
        for i in range(len(arr) - 1 , -1 , -1):
            # currentMax = maxValue
            # if currentMax 
            result[i] = maxValue
            maxValue = max(maxValue,arr[i])
        return result
        
           
            
            
            # i = 0 , i = 1 , i = 2 , i = 3 , i = 4, i = 5
            # currentMax = max(arr[i + 1:])



             # arr[4:] = [1]
            #  currentMax = 1
            # result.append(currentMax)
            # result = [18,6,6,6,1]
        # result =  [18,6,6,6,1]
        # result.append(-1)
       # result =  [18,6,6,6,1,-1]
        # return result





        