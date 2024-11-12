import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


network = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (n + 1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = 1
    for i in network[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)