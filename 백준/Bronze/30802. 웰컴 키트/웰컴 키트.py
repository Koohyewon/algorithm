import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

t_ans = 0
for size in sizes:
    t_ans += (size//t)
    if size % t != 0:
        t_ans += 1

print(t_ans)
print(n // p, n % p)