class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiffer = math.inf

        for i, num in enumerate(nums):
            left_p = i + 1
            right_p = len(nums) - 1
            if i == len(nums) - 2:
                break

            while left_p < right_p:
                currentSum = num + nums[left_p] + nums[right_p]
                if currentSum == target:
                    return target

                if currentSum < target:
                    left_p += 1
                else:
                    right_p -= 1

                diffToTarget = abs(currentSum - target)
                if diffToTarget < minDiffer:
                    result = currentSum
                    minDiffer = diffToTarget
        return result


        

    
        