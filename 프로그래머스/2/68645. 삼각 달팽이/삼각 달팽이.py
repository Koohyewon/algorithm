def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  #아래
                x += 1

            elif i % 3 == 1:    # 오른쪽
                y += 1

            else:   # 왼쪽 위 대각선
                x -= 1
                y -= 1

            triangle[x][y] = num
            num += 1

    answer = []

    for row in triangle:
        answer.extend(row)

    return answer