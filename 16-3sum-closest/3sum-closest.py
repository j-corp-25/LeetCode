class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiffer = math.inf

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            if i == len(nums) - 2:
                break
            left_p = i + 1
            right_p = len(nums) - 1
                
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


        

    
        