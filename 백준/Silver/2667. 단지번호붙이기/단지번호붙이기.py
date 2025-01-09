import sys
sys.setrecursionlimit(10000)

# 상, 하, 좌, 우 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[x][y] = True
    house_count = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '1':
            house_count += dfs(nx, ny)  

    return house_count


N = int(input())
global grid, visited
grid = [list(input().strip()) for _ in range(N)] 
visited = [[False] * N for _ in range(N)] 
complexes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:           
            house_count = dfs(i, j)
            complexes.append(house_count)

print(len(complexes))

for count in sorted(complexes):
    print(count)
