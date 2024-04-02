class Solution:
    def longestPalindrome(self, s: str) -> str:
        # [b,a] , [b,b] , [b,a] = 
        # "babad"
        # ["abcddf"]
        # [babcda]
        # "babad"        
        # "cbbd"
        
        # set up a helper function to check if its palindromic and then base on that decrease from the left
        # use sliding window approach to keep track palindrome inside the window
        # use help palindrome funtion to check if its a palindrome
        # if its not decrease from the left and add from the right,
        # check if its the longest one 
        # initialize an empty string variable
        # if its the longest one, overide the string variable,
        # then return the variable
        longest = ""

        # if len(s) <= 2 and s[0] != s[1]:
        #     return s[0]
        # elif len(s) <= 2 and s[0] != s[1]:
        #     return s[0]
    
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i: j + 1]
                if self.isPalindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
                    

                

    # s = "babad"
    # start = 0
    # end = 1
    # currentPali = "b" + "a" = "ba"

        # while start and end <= len(s):
        #     currentPali = s[start] + s[end] # "ba"
        #     if isPalindrome(currentPali) == True and len(currentPali) > longestPali:
        #         longestPali = currentPali
        #         end += 1
                
        #     else:
        #         end += 1
        #         if not isPalindrome(currentPali):
        #             start += 1
        # return longestPali






    #method #1

    # def isPalindrome(self, string):
    #     left = 0
    #     right = len(string) - 1

    #     while left < right:
    #         if string[left] != string[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    # method #2

    def isPalindrome(self, string):
        return string == string[::-1]

    


    
