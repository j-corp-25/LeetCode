class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left = 0
        # right = len(s) - 1
        # only alphanumeric
        # A-Z,a-z, 0-9, ignore spaces, and anything outside of specified conditions

        # Easy solution
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]