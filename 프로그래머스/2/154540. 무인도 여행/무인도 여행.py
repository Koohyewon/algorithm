from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    answer = []

    # 위, 아래, 왼쪽, 오른쪽
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):

            # 바다거나 이미 방문한 곳이면 넘어감
            if maps[i][j] == 'X' or visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = True

            total = int(maps[i][j])

            while q:
                x, y = q.popleft()

                # 현재 위치에서 상하좌우 확인
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # 지도 밖이면 넘어감
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    # 바다거나 이미 방문했으면 넘어감
                    if maps[nx][ny] == 'X' or visited[nx][ny]:
                        continue

                    # 새로운 땅 방문
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    # 식량 추가
                    total += int(maps[nx][ny])

            answer.append(total)

    if len(answer) == 0:
        return [-1]

    answer.sort()

    return answer