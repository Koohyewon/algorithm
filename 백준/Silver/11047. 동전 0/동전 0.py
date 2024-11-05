import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for i in range(n):
    coins.append(int(sys.stdin.readline().strip()))

coins = list(reversed(coins))  
cnt = 0

for coin in coins:
    if k >= coin:
        cnt += k // coin  
        k %= coin         

print(cnt)
