from collections import deque

cols, rows = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(rows)]
queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_days = 0

for r in range(rows):
    for c in range(cols):
        if box[r][c] == 1:
            queue.append((r, c))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

bfs()

for row in box:
    for cell in row:
        if cell == 0:
            print(-1)
            exit()
    max_days = max(max_days, max(row))

print(max_days - 1)
