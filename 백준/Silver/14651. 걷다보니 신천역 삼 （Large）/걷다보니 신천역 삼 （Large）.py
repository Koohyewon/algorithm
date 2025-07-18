MOD = 10**9 + 9

n = int(input())

if n == 1:
    print(0)
else:
    dp = 2  # N=2일 때 결과
    for i in range(3, n + 1):
        dp = (dp * 3) % MOD
    print(dp)
