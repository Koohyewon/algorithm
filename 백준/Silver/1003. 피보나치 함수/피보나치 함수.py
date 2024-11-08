import sys

MAX_N=40

dp=[[0,0]]*(MAX_N+1)
dp[0]=[1,0]
dp[1]=[0,1]

for i in range(2,MAX_N+1):
    dp[i]=[dp[i-1][0]+dp[i-2][0] , dp[i-1][1]+dp[i-2][1]]

T=int(sys.stdin.readline())
for i in range(T):
    n=int(sys.stdin.readline())
    print(dp[n][0], dp[n][1])