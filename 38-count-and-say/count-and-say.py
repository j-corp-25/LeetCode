class Solution:
    def countAndSay(self, n: int) -> str:
    # input is a number
    # output is a string
    # countandsay(5) one 1, one 2, two 1  = 111221
    # countandsay(6) three 1, two 2, one 1 = 312211
    # base case is 1 , cant be zero
    # 1 = one
    # countAndSay(1) = "1"
    #
        tab = {}
        tab[1] = "1"
        for i in range(2,n + 1):
            lastone = tab[i - 1] # = '3322251'

            # tab[i] = "testing"
            result = ""
            j = 0
            while j < len(lastone): # while 0 less than 7
                currentchar = lastone[j] # current = 3
                k = 1 # 1 count duplicates, k becomes 2
                while (j + k < len(lastone) and lastone[j + k] == currentchar):   # while 0 + 1 less than 7  
                    k += 1
                stringCount = str(k)
                result += stringCount
                result += currentchar
                j += k
            tab[i] = result
        return tab[n]




        
        print(tab)




        