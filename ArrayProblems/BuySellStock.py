class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[0]:
                min = prices[i]
            if prices[i] - min > max:
                profit = prices[i] - min
        return profit


    # Best method to solve the mnaximumsub array problem.
    def maxProfitKdane(self, prices):
        max_cur = 0
        max_global = 0
        for i in range(1, len(prices)):
            max_cur = + prices[i] - prices[i - 1]
            max_cur = max(0, max_cur)
            max_global = max(max_cur, max_global)
        return max_global
