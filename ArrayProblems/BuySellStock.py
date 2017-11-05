class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[0]:
                min = prices[i]
            if prices[i] - min > max:
                profit = prices[i] - min
        return profit
