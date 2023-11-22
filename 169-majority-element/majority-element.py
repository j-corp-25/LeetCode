class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}

        for num in nums:
            if num not in my_map:
                my_map[num] = 1
            else:
                my_map[num] += 1
        
        for char in my_map:
            if my_map[char] > (len(nums) // 2):
                return char
            
        return -1
        