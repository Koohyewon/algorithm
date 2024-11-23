import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    R, S = sys.stdin.readline().split()

    result.append(''.join(i * int(R) for i in S))

sys.stdout.write("\n".join(result) + "\n")
