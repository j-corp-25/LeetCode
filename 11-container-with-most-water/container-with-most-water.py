class Solution:
    def maxArea(self, height: List[int]) -> int:
        # iterate through each one
        # keep track of highest one and second highest
        # small container
        # tall container
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            currentArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currentArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea