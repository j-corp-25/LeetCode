class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        res = 0
        for n in nums:
            seen.add(n)
            if n - diff in seen and n - 2*diff in seen:
                res += 1
        return res