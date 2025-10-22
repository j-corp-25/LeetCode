# Last updated: 10/22/2025, 12:09:12 AM
class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        return (n==1)*1 or [x:={a for a,_ in t}] and next((a for a,f in Counter(b for _,b in t).items() if f==n-1 and a not in x),-1)
        