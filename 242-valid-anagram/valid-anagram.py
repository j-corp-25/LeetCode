class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1

            if t[i] in freq_map:
                freq_map[t[i]] -= 1
            else:
                freq_map[t[i]] = -1

        for char in freq_map:
            if freq_map[char] != 0:
                return False
        
        return True
        