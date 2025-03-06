import sys

input = sys.stdin.read
sys.setrecursionlimit(10000)

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count, total):
    """ DFS를 사용해 테트로미노 4칸을 탐색 """
    global max_value
    if count == 4:  # 4개의 칸을 모두 선택한 경우
        max_value = max(max_value, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, total + grid[nx][ny])
            visited[nx][ny] = False

def check_extra_shapes(x, y):
    """ ㅗ, ㅜ, ㅏ, ㅓ 모양을 체크 """
    global max_value
    for shape in extra_shapes:
        try:
            total = grid[x][y] + grid[x + shape[0][0]][y + shape[0][1]] + \
                    grid[x + shape[1][0]][y + shape[1][1]] + \
                    grid[x + shape[2][0]][y + shape[2][1]]
            max_value = max(max_value, total)
        except IndexError:
            continue  # 범위를 벗어나면 건너뛴다

data = input().split()
N, M = int(data[0]), int(data[1])
grid = []
idx = 2
for i in range(N):
    grid.append(list(map(int, data[idx:idx + M])))
    idx += M

max_value = 0
visited = [[False] * M for _ in range(N)]

# ㅗ, ㅜ, ㅏ, ㅓ 모양을 고려하기 위한 상대 좌표
extra_shapes = [
    [(0, 1), (0, 2), (-1, 1)],  # ㅜ
    [(0, 1), (0, 2), (1, 1)],   # ㅗ
    [(1, 0), (2, 0), (1, 1)],   # ㅏ
    [(1, 0), (2, 0), (1, -1)]   # ㅓ
]

# 모든 위치에서 DFS 탐색 및 ㅗ 모양 체크
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = False
        check_extra_shapes(i, j)

print(max_value)
