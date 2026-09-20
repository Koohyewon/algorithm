def rotate(key):
    m = len(key)
    new_key = []

    for i in range(m):
        row = []
        for j in range(m):
            row.append(key[m - 1 - j][i])
        new_key.append(row)

    return new_key


def check(key, lock, x, y):
    m = len(key)
    n = len(lock)
    size = n + (m - 1) * 2

    # 여백을 둔 판을 만들고 가운데에 자물쇠를 올린다
    board = []
    for i in range(size):
        board.append([0] * size)

    for i in range(n):
        for j in range(n):
            board[m - 1 + i][m - 1 + j] = lock[i][j]

    # (x, y) 위치에 열쇠를 더한다
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] = board[x + i][y + j] + key[i][j]

    # 자물쇠 영역이 전부 1이어야 열린다
    for i in range(n):
        for j in range(n):
            if board[m - 1 + i][m - 1 + j] != 1:
                return False

    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    for turn in range(4):
        if turn > 0:            # 첫 번째는 원래 방향 그대로
            key = rotate(key)

        for x in range(n + m - 1):
            for y in range(n + m - 1):
                if check(key, lock, x, y):
                    return True

    return False