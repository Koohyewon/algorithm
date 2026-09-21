from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):

            if maps[i][j] == 'X' or visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = True

            total = int(maps[i][j])

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if maps[nx][ny] == 'X' or visited[nx][ny]:
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny))

                    total += int(maps[nx][ny])

            answer.append(total)

    if len(answer) == 0:
        return [-1]

    answer.sort()

    return answer