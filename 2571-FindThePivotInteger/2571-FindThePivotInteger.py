# Last updated: 10/22/2025, 12:08:49 AM
class Solution:
    def pivotInteger(self, n: int) -> int:
        for num in range(n+1):
            left = sum(range(1,num+1))
            right = sum(range(num,n+1))
            if left == right:
                return num
        return -1

        