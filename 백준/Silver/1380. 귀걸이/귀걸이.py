import sys
input = sys.stdin.readline

case = 1

while True:
    n = int(input())
    if n == 0:
        break

    names = [input().strip() for _ in range(n)]
    count = [0] * n

    for _ in range(2 * n - 1):
        num, _ = input().split()
        num = int(num) - 1
        count[num] += 1

    for i in range(n):
        if count[i] != 2:
            print(case, names[i])
            break

    case += 1