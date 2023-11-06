class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer is the day we buy
        leftPointer = 0
        # right pointer  is the day we sell
        rightPointer = 1

        # this will track the max profit
        maxProfit = 0

        # continue moving the right pointer until the end of the array
        while rightPointer < len(prices):
            # check if selling is profitable
            if prices[leftPointer] < prices[rightPointer]:
                # calculate the potential profit
                profit = prices[rightPointer] - prices[leftPointer]
                # update the max profit if the current profit is greater than the previous one t
                maxProfit = max(maxProfit, profit)
            else:
                # if selling is not profitable move the buy pointer to the current sell pointer
                leftPointer = rightPointer
                # move the sell pointer to the next day
            rightPointer += 1
        return maxProfit


        