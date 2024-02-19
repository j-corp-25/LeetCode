class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        # put all the numbers in a set {1,3,5,7,9}
        count = 0
        # return a count at the end
        for num in nums:
            # iterate through each number in the nums array
            if (num + diff) in s and (num + 2*diff) in s:
                # here we check if 1 + 2 = 3 is in the set which it is. then we check 1 + 2*2 = 5. 
                # 
                count += 1
        return count