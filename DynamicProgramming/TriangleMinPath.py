class Solution(object):
    def minimumTotal(self, triangle):

        # Base case for empty list
        if len(triangle) == 0:
            return -1

        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(0, i + 1):
                x = float("INF")
                if j <= i - 1:
                    x = min(x, triangle[i - 1][j])
                if j - 1 >= 0:
                    x = min(x, triangle[i - 1][j - 1])

                triangle[i][j] += x
        return min(triangle[-1])
