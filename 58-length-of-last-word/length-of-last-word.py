class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #input string of words with spaces
        # output is integer length of the last word
        # use an array to store the words
        return len(s.strip().split(" ")[-1])

    
       
            






        