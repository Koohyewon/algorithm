import sys
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, field, m, n):
    queue = deque([(x, y)])
    field[y][x] = 0 
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 1:
                field[ny][nx] = 0 
                queue.append((nx, ny))

T = int(sys.stdin.readline())  
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    
    field = [[0] * m for _ in range(n)] 
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1  
    
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(j, i, field, m, n)
                count += 1  
    
    print(count)