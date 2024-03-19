class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # n is the range of the numbers form [1,n]
        # find the sum of the numbers that not divisible by m = num1
        # find the sum of the numbers that are divisible by m  = num2
        # then i will return num1 - num2
        # create a range that i will loop through and i will use n(1, n)
        num1=num2=0
        for i in range(1,n + 1):
            if i%m == 0:
                num2 += i
            else:
                num1 += i
        return num1-num2



            
        