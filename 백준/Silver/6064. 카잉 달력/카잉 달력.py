import sys

def find_year(M, N, x, y):
    while x <= M * N:
        if (x - 1) % N + 1 == y:
            return x
        x += M
    return -1


T = int(sys.stdin.readline().strip())
results = []
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    results.append(str(find_year(M, N, x, y)))

sys.stdout.write("\n".join(results) + "\n")
