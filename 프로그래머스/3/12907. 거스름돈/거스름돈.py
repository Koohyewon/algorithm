def solution(n, money):
    dp = []
    for i in range(n + 1):
        dp.append(0)

    dp[0] = 1   # 0원을 만드는 방법은 "아무것도 안 주기" 1가지

    for coin in money:
        for price in range(coin, n + 1):
            dp[price] = dp[price] + dp[price - coin]
            dp[price] = dp[price] % 1000000007

    return dp[n]