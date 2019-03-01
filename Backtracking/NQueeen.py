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
            x = ["".join(matrix[i]) for i in range(n)]
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


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(row, result, n, dig1, dig2, col_map):
            if row == n:
                result[0] += 1
                return

            for col in range(0, n):

                id1 = col - row + n
                id2 = col + row

                #                 isValid step
                if dig1[id1] or dig2[id2] or col_map[col]:
                    continue

                dig1[id1], dig2[id2], col_map[col] = 1, 1, 1
                backtrack(row + 1, result, n, dig1, dig2, col_map)
                dig1[id1], dig2[id2], col_map[col] = 0, 0, 0

        result = [0]
        dig1, dig2, col_map = [0] * (2 * n), [0] * (2 * n), [0] * n
        backtrack(0, result, n, dig1, dig2, col_map)
        return result[0]
