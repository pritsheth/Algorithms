def combinationSum(candidates, target):
    d = {candidates[i]: 1 for i in range(len(candidates))}
    dp = [0] * (target+1)
    for ch in candidates:
        dp[ch] = 1

    for x in range(1, target+1):
        for coin in candidates:
            if x - coin > 0 and dp[x-coin] != 0:
                dp[x] += dp[x - coin]

    print(dp)
    return dp[target]


combinationSum([2, 3, 7], 7)
