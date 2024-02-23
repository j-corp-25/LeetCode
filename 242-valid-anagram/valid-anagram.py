class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two inputs. s string and t string
        # return true if every character is used atleast once, otherwise return false
        # I can use two hashes and then compare their key value pairs if they are equal

        countS, countT = {},{}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1

        for key in countS:
            if countS[key] != countT.get(key,0):
                return False
        return True

        
        