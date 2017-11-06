class Solution:
    def minimumTotal(self, triangle):
        rows = len(triangle)
        dp = [[]]

        for i in range(rows):
            for j in range(i + 1):
                # if(i-1>=0)
                triangle[i][j] = min(min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i - 1][j + 1])


        """
        :type triangle: List[List[int]]
        :rtype: int
        """
