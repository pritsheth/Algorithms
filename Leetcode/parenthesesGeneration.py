class Solution:
    def generateParenthesis(self, n):
        answer = []
        self.combi(n, 0, 0, "", answer)
        print(answer)

        """
        :type n: int
        :rtype: List[str]
        """

    def combi(self, n, open, close, temp, answer):

        if close == n:
            answer.append(temp)

        if open < n:
            self.combi(n, open + 1, close, temp + '(', answer)
        if open > close and close < n:
            self.combi(n, open, close + 1, temp + ')', answer)


s = Solution()
s.generateParenthesis(4)
