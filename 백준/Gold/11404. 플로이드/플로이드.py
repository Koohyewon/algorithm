maxDis = 1000000000


def floyd():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]


def printd():
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if d[y][x] == maxDis:
                d[y][x] = 0
            print(d[y][x], end=" ")
        print()


n = int(input())
m = int(input())
d = [[maxDis] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())

    if d[a][b] != maxDis:
        d[a][b] = min(d[a][b], c)
        continue

    d[a][b] = c

floyd()

printd()
