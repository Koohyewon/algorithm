from collections import deque

def bfs(maps, start, end):
    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append((start[0], start[1], 0))

    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, dist = q.popleft()

        if (x, y) == end:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i, j)
            elif maps[i][j] == 'L':
                l = (i, j)
            elif maps[i][j] == 'E':
                e = (i, j)

    d1 = bfs(maps, s, l)
    d2 = bfs(maps, l, e)

    if d1 == -1 or d2 == -1:
        return -1

    return d1 + d2