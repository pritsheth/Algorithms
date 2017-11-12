class Solution(object):
    def numDecodings(self, s):

        length = len(s)
        if s == None or length == 0:
            return 0

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1 if s[0:1] != '0' else 0

        for i in range(2, len(s) + 1):
            a1, a2 = int(s[i - 1]), int(s[i - 2:i])

            if a2 >= 10 and a2 <= 26:
                dp[i] = dp[i] + dp[i - 2]

            if a1 >= 1 and a1 <= 9:
                dp[i] = dp[i] + dp[i - 1]

        print(dp)
        return dp[len(s)]
