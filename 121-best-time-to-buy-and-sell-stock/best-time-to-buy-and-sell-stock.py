class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input is an array
        maxProfit = 0
        l = 0 #buy
        r = 1 #sell

        while r <= len(prices) - 1:
            currentProfit = prices[r] - prices[l]
            if prices[r] > prices[l]: # check if you can sell it more than you bought it more
                maxProfit = max(maxProfit,currentProfit)
            else:
                l = r
            r += 1
        return maxProfit
  


        