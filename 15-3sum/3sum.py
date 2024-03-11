class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0 :
                break
            if i > 0 and num == nums[i - 1]:
                continue
            left_p = i + 1
            right_p = len(nums) - 1
            while left_p < right_p:
                threesum = num + nums[left_p] + nums[right_p]

                if threesum > 0:
                    right_p -= 1
                elif threesum < 0:
                    left_p += 1
                else:
                    triplets.append([num,nums[left_p], nums[right_p]])
                    left_p += 1
                    while (left_p < right_p and nums[left_p] == nums[left_p - 1]):
                        left_p += 1
        return triplets
