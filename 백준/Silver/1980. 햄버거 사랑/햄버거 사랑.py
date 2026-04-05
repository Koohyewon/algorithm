n, m, t = map(int, input().split())

dp = [-1] * (t + 1)
dp[0] = 0

for i in range(t + 1):
    if dp[i] == -1:
        continue
    
    if i + n <= t:
        dp[i + n] = max(dp[i + n], dp[i] + 1)
    if i + m <= t:
        dp[i + m] = max(dp[i + m], dp[i] + 1)

for i in range(t, -1, -1):
    if dp[i] != -1:
        print(dp[i], t - i)
        break