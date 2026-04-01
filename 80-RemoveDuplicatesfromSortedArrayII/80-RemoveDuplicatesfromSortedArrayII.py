# Last updated: 3/31/2026, 11:19:20 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 1
4        count = 1
5
6        for index in range(1,len(nums)):
7            if nums[index] == nums[index - 1]:
8                count += 1
9            else:
10                count = 1
11                
12            if count <= 2:
13                nums[k] = nums[index]
14                k += 1
15        return k
16