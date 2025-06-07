import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

dx=[1, 0]
dy=[0, 1]

visited = [[False]*n for _ in range(m)]
queue = deque()
queue.append((0, 0))
visited[0][0] = True

found=False

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        found=True
        break

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))

print("Yes" if found else "No")