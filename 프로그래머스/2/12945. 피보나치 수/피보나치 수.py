def solution(n):
    dp = []
    for i in range(n + 1):
        dp.append(0)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] = dp[i] % 1234567

    return dp[n]