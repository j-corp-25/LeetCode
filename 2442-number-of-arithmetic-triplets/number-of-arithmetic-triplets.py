class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        # put all the numbers in a set {1,3,5,7,9}
        count = 0
        # return a count at the end
        for i in range(len(nums)):
            # iterate through each number in the nums array
            if (nums[i] + diff) in s and (nums[i] + 2*diff) in s:
                # here we check if (current num)1 + 2 = 3 is in the set which it is. then we check 1 + 2*2 = 5. which is also in the set we then increment count
                count += 1
        return count