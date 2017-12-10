def isMatching(A, pat):
    m = len(A)
    n = len(pat)

    dp = [[0] * n for i in range(m)]

    if A[0] == pat[0] or pat[0] == '.' or pat[0] == '*':
        dp[0][0] = 1

    # Pattern :-
    for i in range(1, m):
        if pat[i] == '*':
            dp[i][0] = dp[i - 1][0]
        if pat[i] == '.':
            dp[i][0] = dp[i - 1][0]

    for j in range(1, m):
        if pat[0] == '*':
            dp[0][j] = 1
        if pat[0] == '.':
            dp[0][j] = dp[0][j - 1]



    for i in range(m):
        for j in range(n):
            if pat[i] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif pat[i] == '*':
                dp[i][j] = dp[i - 1][i - 1]
            elif pat[i] != A[j]:
                dp[i][j] = 0
            elif pat[i] == A[i]:
                dp[i][j] = dp[i - 1][j - 1]


isMatching('abc', 'ab')
