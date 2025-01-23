n = int(input())  # n 크기 입력
m = input()  # 이동 방향 입력

ud = [[False] * (n) for _ in range(n)]  # 수직
lr = [[False] * (n) for _ in range(n)]  # 수평

row, col = 0, 0  # 처음 위치

# UDLR
for direction in m:
    if direction == 'U':
        if not (0 <= row-1 < n) or not (0 <= col < n):
            continue
        ud[row][col] = True
        row -= 1
        ud[row][col] = True

    elif direction == 'D':
        if not (0 <= row+1 < n) or not (0 <= col < n):
            continue
        ud[row][col] = True
        row += 1
        ud[row][col] = True

    elif direction == 'L':
        if not (0 <= row < n) or not (0 <= col-1 < n):
            continue
        lr[row][col] = True
        col -= 1
        lr[row][col] = True

    elif direction == 'R':
        if not (0 <= row < n) or not (0 <= col+1 < n):
            continue
        lr[row][col] = True
        col += 1
        lr[row][col] = True

for i in range(n):
    for j in range(n):
        if ud[i][j] and lr[i][j]:
            print('+', end='')
        elif ud[i][j]:
            print('|', end='')
        elif lr[i][j]:
            print('-', end='')
        else:
            print('.', end='')
    print()