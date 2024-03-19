class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # n is the range of the numbers form [1,n]
        # find the sum of the numbers that not divisible by m = num1
        # find the sum of the numbers that are divisible by m  = num2
        # then i will return num1 - num2
        # create a range that i will loop through and i will use n(1, n)
        num1,num2 = [], []
        for i in range(1,n + 1):
            if not i % m == 0:
                num1.append(i)
            else:
                num2.append(i)
            
        result1 = sum(num1)
        result2 = sum(num2)
        result = (result1 - result2)
        return result


            
        