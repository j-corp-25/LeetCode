class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        # nums = [1,2,3,4]
        # [1,2] , [3,4]
        # answer = [2,4,4,4]

        # [1,1,2,3]
        # answer = [1,3,3]
        # answer = []
        # start = 0
        # next = start + 1
        # next < len(nums)
        # append(nums[i + 1] * nums[i])
        # for loop to iterate through the numbers
            # FreqTime = 
            # freq = nums[i]
            # val = nums[i + 1]
            # while freq > 0:
                # answer.append(val)
                # freq -= 1
        answer = []
        for i in range(0,len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            while freq > 0:
                answer.append(val)
                freq -= 1
        
        return answer