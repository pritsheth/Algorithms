import copy

class Solution(object):

    def isValid(self, matrix, row, col, n):

        #         Check for row:

        for i in range(0, row):
            if matrix[i][col] == 'Q':
                return False

        # left diagonal
        x, y = row - 1, col - 1
        while x >= 0 and y >= 0:
            if matrix[x][y] == 'Q':
                return False
            x -= 1
            y -= 1

        x, y = row - 1, col + 1
        while x >= 0 and y < n:
            if matrix[x][y] == 'Q':
                return False
            x -= 1
            y += 1

        return True

    def createCombination(self, matrix, n, row, result):

        if n == row:
            print("solution")
            x = [ "".join(matrix[i])  for i in range(n)]
            result.append(x)
            return

        for j in range(n):

            if self.isValid(matrix, row, j, n):
                matrix[row][j] = 'Q'
                self.createCombination(matrix, n, row + 1, result)
                matrix[row][j] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        matrix = [['.'] * n for i in range(n)]
        self.createCombination(matrix, n, 0, result)
        print(result)
        return result


s = Solution()
s.solveNQueens(4)
