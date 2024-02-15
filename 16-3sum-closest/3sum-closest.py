class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)-2):
            left_pointer = i + 1
            right_pointer = len(nums) - 1


            while left_pointer < right_pointer:
                currentSum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if abs(currentSum - target) < abs(res-target):
                    res = currentSum
                if currentSum < target:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return res

        