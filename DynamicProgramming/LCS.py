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


print(find_length_lcs([2, 3, 1], [1, 2, 3]))
