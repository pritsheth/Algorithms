from collections import Counter


class cluster:

    def __init__(self, m, n):
        no = m * n
        self.dp = [-1 for _ in range(no)]
        self.size = [0 for _ in range(no)]
        self.m = m
        self.n = n

    def getID(self, point):
        return self.n * point[0] + point[1]

    def printSize(self):
        print(self.dp)
        print(self.size)

    def getIslands(self):
        s = set()
        for no in self.dp:
            if no >= 0:
                s.add(self.find(no))

        print(s)
        return len(s)

    def setSize(self, point):
        id = self.getID(point)
        self.dp[id] = id
        self.size[id] = 1

    def union(self, point1, point2):

        id1 = self.getID(point1)
        id2 = self.getID(point2)

        rootA = self.find(id1)
        rootB = self.find(id2)

        self.dp[rootA] = rootB
        self.size[rootB] += self.size[rootA]

    def find(self, id):

        if self.dp[id] == id:
            return id
        else:
            return self.find(self.dp[id])


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        c = cluster(m, n)
        grid = [[0] * n for i in range(m)]
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = []
        for x, y in positions:
            grid[x][y] = 1
            c.setSize((x, y))

            for d in dir:
                newx, newy = x + d[0], y + d[1]
                if 0 <= newx < m and 0 <= newy < n:
                    if grid[newx][newy] == 1:
                        c.union((x, y), (newx, newy))

            result.append(c.getIslands())
            print(result)
        return result


s = Solution()
s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
