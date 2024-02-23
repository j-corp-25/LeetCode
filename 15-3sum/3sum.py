class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        newArray = []
        for i, a in  enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left_pointer, right_pointer = i + 1, len(nums) - 1
            while left_pointer < right_pointer:
                threeSum = a + nums[left_pointer] + nums[right_pointer]
                if threeSum > 0:
                    right_pointer -= 1
                elif threeSum < 0:
                    left_pointer += 1
                else:
                    newArray.append([a,nums[left_pointer],nums[right_pointer]])
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
        return newArray






        