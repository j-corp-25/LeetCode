class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHashA, myHashB = {}, {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in myHashA:
                myHashA[char] += 1
            else:
                myHashA[char] = 1

        for char in t:
            if char in myHashB:
                myHashB[char] += 1
            else:
                myHashB[char] = 1
                
        if myHashB == myHashA:
            return True



        