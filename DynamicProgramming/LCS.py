# Longest common sub sequence:
def find_length_lcs(a1, a2):
    dp = [[0 for i in range(len(a1) + 1)] for j in range(len(a2) + 1)]

    for i in range(1, len(a1) + 1):
        for j in range(1, len(a2) + 1):
            if a1[i - 1] == a2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(a1)][len(a1)]


print(find_length_lcs([1, 5, 2, 6, 3, 7], [5, 6, 7, 1, 2, 3]))
