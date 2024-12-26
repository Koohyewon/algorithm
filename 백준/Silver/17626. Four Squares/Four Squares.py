import math

n = int(input().strip())

dp = [float('inf')] * (n + 1)
dp[0] = 0

squares = []
for i in range(1, int(math.sqrt(n)) + 1):
    squares.append(i * i)

for square in squares:
    for i in range(square, n + 1):
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])
