import sys

remain=dict()

for _ in range(10):
    n=int(sys.stdin.readline())
    remain[n%42] = 1

print(len(remain.keys()))