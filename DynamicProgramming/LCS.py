# Longest common sub sequence:
def find_length_lcs(a1, a2):
    N = len(a1)
    dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if a1[i - 1] == a2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp)
    return dp[N][N]


# print(find_length_lcs([2, 3, 1], [1, 2, 3]))


def find_least_slice(matrix, N):
    dp = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        dp[0][i] = matrix[0][i]

    for i in range(1, N):
        for j in range(N):
            left = float("INF")
            right = float("INF")
            if (j - 1 >= 0):
                left = dp[i - 1][j - 1]
            if j + 1 < N:
                right = dp[i - 1][j + 1]
            dp[i][j] = matrix[i][j] + min(left, min(dp[i - 1][j], right))

    print(dp[N-1][:])
    return min(dp[N-1][:])


print(find_least_slice(([1, 2, 3], [4, 5, 6], [7, 8, 9]), 3))
