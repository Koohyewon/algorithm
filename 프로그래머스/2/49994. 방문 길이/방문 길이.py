def solution(dirs):
    x = 0
    y = 0
    visited = set()
    move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }

    answer = 0

    for direction in dirs:
        nx = x + move[direction][0]
        ny = y + move[direction][1]

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        road1 = (x, y, nx, ny)
        road2 = (nx, ny, x, y)

        if road1 not in visited:
            visited.add(road1)
            visited.add(road2)
            answer += 1

        x = nx
        y = ny

    return answer