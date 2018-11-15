class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def recur(open, close, n, temp, res):

            if len(temp) == 2 * n:
                res.append(temp[:])
                return

            if open < n:
                recur(open + 1, close, n, temp + '(', res)
            if open > close:
                recur(open, close + 1, n, temp + ')', res)

            return

        res = []
        recur(0, 0, n, "", res)
        print(res)
        return res


s = Solution()
s.generateParenthesis(3)
