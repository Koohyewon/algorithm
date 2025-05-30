import sys

input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c][d]: (r, c)에 방향 d(0:가로, 1:세로, 2:대각선)로 파이프가 올 수 있는 경우의 수
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 시작 위치
dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if house[r][c] == 1:
            continue
        # 가로
        dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
        # 세로
        if r > 0:
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
        # 대각선
        if r > 0 and house[r-1][c] == 0 and house[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))