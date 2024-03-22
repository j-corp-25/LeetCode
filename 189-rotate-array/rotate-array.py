class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # grab the last elements base on k, [5,6,7]
        #[:-3]
        # grab the last 3
        # shift them into the front the array
        # pop the the last 3
        # if k == 0 return array
        # nums == 6, k == 6.
        # 8 % len(nums) == 2
        # last 2 elements

        if k == len(nums):  # [1,2,3,4,5,6,7], k = 3 , len(nums) = 7
            return nums
        if k == 0:
            return nums
        if k > len(nums):
            k = k % len(nums)
        
        lastKs = nums[-k:] # [5,6,7], k = 3
        for i in range(len(lastKs)): # [5,6,7], i = 1, lastKs[1] = 6
            nums.insert(i,lastKs[i]) # 0, lastKs[0] == 5 , [5,1,2,3,4,5,6,7], [5,6,1,2,3,4,5,6]
            nums.pop() # [5,1,2,3,4,5,6] , [5,6,1,2,3,4,5], [5,6,7,1,2,3,4]
        





 # [1,2,3,4,5,6,7], k = 3 

 # step 1 : reverse array
 # [7,6,5,4,3,2,1]
 #step 2 : reverse  first k elements
 # nums[:k] == reversed(nums[:k])
# [5,6,7]
#then reverse from k + 1, remaining in nums
# from k up to len(nums)
# [5,6,7,1,2,3,4]

 

        

          

        