import sys
from collections import deque

a,b,n,m=map(int, sys.stdin.readline().split())
dp = dict()
dp[n] = 0
queue = deque([n])

while queue:
    current = queue.popleft()

    for i in range(8):
        move = [current+1,current-1,current*a,current*b,current+a,current-a,current+b,current-b]
        val = move[i]
        if 0 <= val <= 100000 and val not in dp:
            dp[val] = dp[current] + 1
            queue.append(val)

    if m in dp:
        break
    
print(dp[m])