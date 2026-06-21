from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    # 시작 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                sx, sy = i, j

    q = deque([(sx, sy, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, cnt = q.popleft()

        if board[x][y] == "G":
            return cnt

        for d in range(4):
            nx, ny = x, y

            # 벽 또는 장애물 만날 때까지 이동
            while True:
                tx = nx + dx[d]
                ty = ny + dy[d]

                if not (0 <= tx < n and 0 <= ty < m):
                    break

                if board[tx][ty] == "D":
                    break

                nx, ny = tx, ty

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return -1