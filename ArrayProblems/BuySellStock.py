class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
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

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

    def maxProfitWithMultipleSell(self, prices):

        """
        :type prices: List[int]
        :rtype: int
        """

        for i in range(len(prices)):



    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/


    def maxProfitWithFees(prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        max_cur = 0
        max_global = 0
        for i in range(1, len(prices)):
            max_cur += prices[i] - prices[i - 1]
            max_cur = max(0, max_cur)
            max_global = max(max_global, max_cur)
        print("total profit", max_global)

    maxProfitWithFees([1, 3, 2, 8, 4, 9], 2)
