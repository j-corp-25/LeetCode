class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left = 0
        # right = len(s) - 1
        # only alphanumeric
        # A-Z,a-z, 0-9, ignore spaces, and anything outside of specified conditions

        # Easy solution #1
        # new_str = ""
        # for c in s:
        #     if c.isalnum():
        #         new_str += c.lower()
        # return new_str == new_str[::-1]

        # Medium solution #1

        left, right = 0,len(s) - 1
        while left < right:
            while left < right and self.checkifAlphanum(s[left]) == False:
                left += 1
            while right > left and self.checkifAlphanum(s[right]) == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            

    def checkifAlphanum(self, char):
        return (
            ord("A") <= ord(char) <= ord("Z")
            or ord("0") <= ord(char) <= ord("9")
            or ord("a") <= ord(char) <= ord("z")
        )
