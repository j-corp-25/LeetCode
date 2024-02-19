class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        
        for i in range(len(words)):
            l = 0
            r = len(words[i]) - 1
            while l < r:
                if words[i][l] != words[i][r]:
                    break
                l += 1
                r -= 1
            if l >= r:
                return words[i]
            

            
        return ""
                
                    
        
        


        
        