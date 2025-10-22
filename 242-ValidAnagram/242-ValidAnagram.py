# Last updated: 10/22/2025, 12:09:41 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHashA, myHashB = {}, {}

        if len(s) != len(t):
            return False

        for char in s:
            myHashA[char] = myHashA.get(char, 0) + 1

        for char in t:
            myHashB[char] = myHashB.get(char, 0) + 1

        return myHashB == myHashA
