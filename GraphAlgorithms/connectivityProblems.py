class Solution:
    def exist(self, board, word):
        x = False
        visited = [False * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    x = x | self.dfs(board, word, i, j, 1, visited)
        return x

    def dfs(self, b, word, i, j, index, visited):

        x = False
        if index == len(word):
            return True

        if i == -1 or i == len(b) or j == -1 or j == len(b[0]) or visited[i][j]:
            return False

        visited[i][j] = True
        if b[i - 1][j] == word[index]:
            x |= self.dfs(b, word, i - 1, j, index + 1, visited)
        if b[i][j - 1] == word[index]:
            x |= self.dfs(b, word, i, j - 1, index + 1, visited)
        if b[i + 1][j] == word[index]:
            x |= self.dfs(b, word, i + 1, j, index + 1, visited)
        if b[i][j + 1] == word[index]:
            x |= self.dfs(b, word, i, j + 1, index + 1, visited)

        return x

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

()