class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.result = []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.addCombination([], digits, d, 0, len(digits), res)
        print(res)
        return res

    def addCombination(self, text, digits, d, mapIndex, length, res):

        if len(text) == length:
            res.append(''.join(text))
            return

        l = d[(digits[mapIndex])]
        for i in range(len(l)):
            text.append(l[i])
            self.addCombination(text, digits, d, mapIndex + 1, length, res)
            text.pop()

        """
        :type digits: str
        :rtype: List[str]
        """
s = Solution()
s.letterCombinations("23")